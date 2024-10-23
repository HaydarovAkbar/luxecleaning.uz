from telegram.ext import CallbackContext
from django.conf import settings
from django.utils import timezone
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

from .keyboards import Keyboards as kb
from .messages import Messages as msg
from ..states import States as state

from apps.models import TgUsers, Footer, Stock, FAQ, TgServices, TgServicesPrice, Orders

import re


def remove_html_tags(text):
    # Use regex to remove all tags between < and >
    clean_text = re.sub(r'<.*?>', '', text)
    return clean_text


def start(update: Update, context: CallbackContext):
    user_db = TgUsers.objects.filter(chat_id=update.message.chat_id)
    if user_db.exists():
        user_db = user_db.first()
        lang = user_db.lang
        update.message.reply_html(msg().base.get(lang), reply_markup=kb.base(lang))
        return state.GET_MENU
    else:
        user_defualt_language = update.message.from_user.language_code
        if not user_defualt_language in ['uz', 'ru']:
            user_defualt_language = 'ru'
        update.message.reply_html(msg().start.get(user_defualt_language), reply_markup=kb.language())
        return state.GET_LANG


def get_lang(update: Update, context: CallbackContext):
    query = update.callback_query
    lang = query.data
    user_db, create = TgUsers.objects.get_or_create(chat_id=query.message.chat_id, defaults={
        'lang': lang,
        'username': query.from_user.username,
        'first_name': query.from_user.first_name,
        'last_name': query.from_user.last_name,
    })
    if not create:
        user_db.lang = lang
        user_db.save()
    query.message.delete()
    context.bot.send_message(chat_id=query.message.chat_id, text=msg().base.get(lang), reply_markup=kb.base(lang))
    return state.GET_MENU


def about(update: Update, context: CallbackContext):
    user_db = TgUsers.objects.get(chat_id=update.message.chat_id)

    update.message.reply_text(msg().about.get(user_db.lang))
    return state.GET_MENU


def user_settings(update: Update, context: CallbackContext):
    user_db = TgUsers.objects.get(chat_id=update.message.chat_id)
    update.message.reply_html(msg().settings.get(user_db.lang), reply_markup=ReplyKeyboardRemove())
    update.message.reply_html(msg().choose_language.get(user_db.lang), reply_markup=kb.language())
    return state.CHANGE_LANG


def change_lang(update: Update, context: CallbackContext):
    query = update.callback_query
    lang = query.data
    user_db = TgUsers.objects.get(chat_id=query.message.chat_id)
    user_db.lang = lang
    user_db.save()
    query.message.delete()
    context.bot.send_message(chat_id=query.message.chat_id, text=msg().succes_msg.get(lang), reply_markup=kb.base(lang))
    return state.GET_MENU


def help(update: Update, context: CallbackContext):
    update.message.reply_text(msg().help.get(update.message.from_user.language_code))
    return state.START


### Corporate clients methods ###

def corporate_clients(update: Update, context: CallbackContext):
    user_db = TgUsers.objects.get(chat_id=update.message.chat_id)
    bot_msg = msg().corporate_clients.get(user_db.lang).format(user_db.get_full_name(), Footer.objects.first().phone2)

    update.message.reply_html(bot_msg, reply_markup=kb.back(user_db.lang))
    return state.CORPORATE_CLIENTS


def get_corporate_phone(update: Update, context: CallbackContext):
    user_db = TgUsers.objects.get(chat_id=update.message.chat_id)
    user_db.phone = update.message.contact.phone_number
    user_db.save()
    corporate_client = """
Korporativ mijoz:

👤 {}
📞 {}
📅 {}
"""
    try:
        context.bot.send_message(chat_id=settings.CHANNEL_ID,
                                 text=corporate_client.format(user_db.get_full_name(), user_db.phone,
                                                              user_db.get_created_at()))
    except Exception as e:
        print(e)
    update.message.reply_html(msg().succesfuly_corporate_clients.get(user_db.lang), reply_markup=kb.base(user_db.lang))
    return state.GET_MENU


def corporative_client_msg(update: Update, context: CallbackContext):
    user_db = TgUsers.objects.get(chat_id=update.message.chat_id)

    button = InlineKeyboardButton(
        text=f"Xabar egasi: {update.message.from_user.first_name}",
        url=f"tg://user?id={update.message.from_user.id}"
    )
    reply_markup = InlineKeyboardMarkup([[button]])

    try:
        update.message.copy(
            chat_id=settings.CHANNEL_ID,
            reply_markup=reply_markup
        )
    except Exception as e:
        print(e)

    update.message.reply_html(msg().succesfuly_corporate_clients.get(user_db.lang), reply_markup=kb.base(user_db.lang))
    return state.GET_MENU


### End of Corporate clients methods ###


### Stock methods ###
def discount(update: Update, context: CallbackContext):
    user_db = TgUsers.objects.get(chat_id=update.message.chat_id)
    bot_msg = msg().discount.get(user_db.lang)
    discount_msg, i = '', 1
    for dis in Stock.objects.all():
        _ = msg.numbers.get(str(i))
        if user_db.lang == 'uz':
            discount_msg += f"{_}. <b>{dis.title_uz}</b> - {dis.description_uz}\n\n"
        else:
            discount_msg += f"{_}. <b>{dis.title_ru}</b> - {dis.description_ru}\n\n"
        i += 1
    update.message.reply_html(bot_msg.format(discount_msg), reply_markup=kb.back(user_db.lang))
    return state.GET_MENU


### End of Stock methods ###

### FAQ and connection with manager methods ###
def faq_and_connection(update: Update, context: CallbackContext):
    user_db = TgUsers.objects.get(chat_id=update.message.chat_id)
    faq_msg, i = '', 1
    for f in FAQ.objects.all():
        _ = msg.numbers.get(str(i))
        if user_db.lang == 'uz':
            faq_msg += f"{_}. <b>{remove_html_tags(f.question_uz)}</b>\n{remove_html_tags(f.answer_uz)}\n\n"
        else:
            faq_msg += f"{_}. <b>{remove_html_tags(f.question)}</b>\n{remove_html_tags(f.answer)}\n\n"
        i += 1
    bot_msg = msg().faq_and_connection.get(user_db.lang).format(faq_msg, Footer.objects.first().phone2)
    update.message.reply_html(bot_msg, reply_markup=kb.back(user_db.lang))
    return state.GET_MENU


### End of FAQ and connection with manager methods ###

### contact methods ###

def contact(update: Update, context: CallbackContext):
    user_db = TgUsers.objects.get(chat_id=update.message.chat_id)
    bot_msg = msg().get_contact_msg_uz(Footer.objects.first()) if user_db.lang == 'uz' else msg().get_contact_msg_ru(
        Footer.objects.first())
    update.message.reply_html(bot_msg, reply_markup=kb.back(user_db.lang))
    return state.GET_MENU


### End of contact methods ###


### Service and price methods ###
def service_and_price(update: Update, context: CallbackContext):
    user_db = TgUsers.objects.get(chat_id=update.message.chat_id)
    _service_ = TgServices.objects.all()

    service_pr = ""

    bot_msg = msg().service_price.get(user_db.lang)
    update.message.reply_html(bot_msg, reply_markup=kb.back(user_db.lang))
    return state.GET_MENU


def services(update: Update, context: CallbackContext):
    user_db = TgUsers.objects.get(chat_id=update.message.chat_id)
    update.message.reply_html(msg().btv.get(user_db.lang), reply_markup=ReplyKeyboardRemove())
    # context.bot.delete_message(chat_id=a.chat_id, message_id=a.message_id)
    update.message.reply_html(msg().get_service_type.get(user_db.lang),
                              reply_markup=kb.get_service_types(TgServices.objects.all(), user_db.lang))
    return state.GET_SERVICE_TYPE


def get_service_type(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == 'back':
        user_db = TgUsers.objects.get(chat_id=query.message.chat_id)
        query.delete_message()
        context.bot.send_message(chat_id=user_db.chat_id, text=msg().base.get(user_db.lang),
                                 reply_markup=kb.base(user_db.lang))
        return state.GET_MENU
    service_id = query.data
    context.chat_data['service_id'] = service_id
    user_db = TgUsers.objects.get(chat_id=query.message.chat_id)
    query.delete_message()
    context.bot.send_message(chat_id=user_db.chat_id, text=msg.get_service_type_msg.get(user_db.lang),
                             reply_markup=kb.phone_number_service(user_db.lang), parse_mode="HTML")
    return state.GET_PHONE_NUMBER


def change_phone_number(update: Update, context: CallbackContext):
    user_db = TgUsers.objects.get(chat_id=update.message.chat_id)
    user_db.phone_number = update.message.contact.phone_number
    user_db.save()
    update.message.reply_html(msg().get_full_name.get(user_db.lang), reply_markup=kb.back(user_db.lang))
    return state.GET_NAME


def get_full_name(update: Update, context: CallbackContext):
    user_db = TgUsers.objects.get(chat_id=update.message.chat_id)
    update.message.reply_html(msg().get_full_name.get(user_db.lang), reply_markup=kb.back(user_db.lang))
    return state.GET_NAME


def re_phone(update: Update, context: CallbackContext):
    user_db = TgUsers.objects.get(chat_id=update.message.chat_id)
    user_msg = update.message.text
    re_phone = re.compile(r'^\+998\d{9}$')
    if re_phone.match(user_msg):
        user_db.phone_number = user_msg
        user_db.save()
        update.message.reply_html(msg().change_phone_success.get(user_db.lang), reply_markup=kb.back(user_db.lang))
        return state.GET_NAME
    else:
        update.message.reply_html(msg().wrong_phone.get(user_db.lang),
                                  reply_markup=kb.phone_number_service(user_db.lang))
        return state.GET_PHONE_NUMBER


def get_name(update: Update, context: CallbackContext):
    user_db = TgUsers.objects.get(chat_id=update.message.chat_id)
    user_db.full_name = update.message.text
    user_db.save()

    button = InlineKeyboardButton(
        text=f"Xabar egasi: {update.message.from_user.first_name}",
        url=f"tg://user?id={update.message.from_user.id}"
    )
    user_service = TgServices.objects.get(id=context.chat_data['service_id'])
    reply_markup = InlineKeyboardMarkup([[button]])
    bot_msg = """
Murojaat kelib tushdi!

👤 Familiya Ism: {}
♻️ Xizmat turi: {}
📞 Telefon: {}
📅 Vaqt: {}
""".format(user_db.full_name, user_service.title_uz, user_db.phone_number, user_db.get_created_at())
    try:
        context.bot.send_message(chat_id=settings.CHANNEL_ID, text=bot_msg, reply_markup=reply_markup)
    except Exception as e:
        print(e)
    Orders.objects.create(
        user=user_db,
        service=user_service,
    )
    update.message.reply_html(msg().succesfuly_order.get(user_db.lang) + '\n\n' + msg().get_video.get(user_db.lang),
                              reply_markup=kb.back(user_db.lang))
    return state.GET_VIDEO


def get_video(update: Update, context: CallbackContext):
    user_db = TgUsers.objects.get(chat_id=update.message.chat_id)

    button = InlineKeyboardButton(
        text=f"Xabar egasi: {update.message.from_user.first_name}",
        url=f"tg://user?id={update.message.from_user.id}"
    )
    reply_markup = InlineKeyboardMarkup([[button]])

    try:
        update.message.copy(
            chat_id=settings.CHANNEL_ID,
            reply_markup=reply_markup
        )
    except Exception as e:
        print(e)

    update.message.reply_html(msg().succesfuly_order.get(user_db.lang), reply_markup=kb.back(user_db.lang))
    return state.GET_MENU


def connection_with_admin(update: Update, context: CallbackContext):
    user_db = TgUsers.objects.get(chat_id=update.message.chat_id)
    bot_msg = msg().connection_with_admin.get(user_db.lang)
    update.message.reply_html(bot_msg, reply_markup=kb.back(user_db.lang))
    return state.MESSAGE


def message(update: Update, context: CallbackContext):
    user_db = TgUsers.objects.get(chat_id=update.message.chat_id)

    button = InlineKeyboardButton(
        text=f"Xabar egasi: {update.message.from_user.first_name}",
        url=f"tg://user?id={update.message.from_user.id}"
    )
    reply_markup = InlineKeyboardMarkup([[button]])
    try:
        update.message.copy(
            chat_id=settings.CHANNEL_ID,
            reply_markup=reply_markup
        )
    except Exception as e:
        print(e)

    update.message.reply_html(msg().succesfuly_corporate_clients.get(user_db.lang),
                              reply_markup=kb.back(user_db.lang))
    return state.MESSAGE


def my_orders(update: Update, context: CallbackContext):
    user_db = TgUsers.objects.get(chat_id=update.message.chat_id)
    orders = Orders.objects.filter(user=user_db)
    i = 1
    if user_db.lang == 'uz':
        bot_msg = ""
        for order in orders:
            ord_status = msg().get_order_status(order.status, user_db.lang)
            bot_msg += f"{i}).  <i>{order.service.title_uz}</i>        {order.get_created_at()}    {ord_status}\n"
            i += 1
        result = """
<b>🛀 Sizning buyurtmalaringiz:</b>

№     Xizmat turi       Vaqt          Holati
{}
        """
        bot_msg = result.format(bot_msg)
    else:
        bot_msg = ""
        for order in orders:
            ord_status = msg().get_order_status(order.status, user_db.lang)
            bot_msg += f"{i}).  <i>{order.service.title_ru}</i>        {order.get_created_at()}    {ord_status}\n"
            i += 1
        result = """
<b>🛀 Ваши заказы:</b>

№     Тип услуги       Время          Статус
{}
        """
        bot_msg = result.format(bot_msg)
    update.message.reply_html(bot_msg, reply_markup=kb.back(user_db.lang))
    return state.GET_MENU
