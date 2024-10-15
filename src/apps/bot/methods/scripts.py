from telegram.ext import CallbackContext
from django.conf import settings
from django.utils import timezone
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

from .keyboards import Keyboards as kb
from .messages import Messages as msg
from ..states import States as state

from apps.models import TgUsers, Footer, Stock, FAQ, TgServices, TgServicesPrice

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

    update.message.reply_html(bot_msg, reply_markup=kb.phone_number(user_db.lang))
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
    update.message.reply_html(bot_msg.format(discount_msg), reply_markup=kb.base(user_db.lang))


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


### services methods ###
def services(update: Update, context: CallbackContext):
    user_db = TgUsers.objects.get(chat_id=update.message.chat_id)
    # bot_msg = msg().services.get(user_db.lang)
    _service_ = TgServices.objects.all()

    service_pr = ""  # Initialize the service message

    if user_db.lang == 'uz':
        for ser in _service_:
            # Add service title
            service_pr += "<code>{:^}</code>\n".format(ser.title_uz)
            # service_pr += "{:<15} {:<32} {:<45}\n".format("Size", "Daily", "Monthly")

            # Accumulate prices per service
            for pr in TgServicesPrice.objects.filter(service=ser):
                service_pr += "{:<15} {:<25} {:<35}\n".format(
                    pr.size_uz, pr.daily_price_uz, pr.monthly_price_uz
                )
            service_pr += "\n"  # Add space between services

            # Final message with services list
        bot_msg = """
<b>Xizmatlarimizga qiziqish bildirganingiz uchun tashakkur!</b>

Hozir biz taklif qilayotgan xizmatlar:
<code>{:<4}      {:<15}        {:<25}</code>

{}
Qo'shimcha ma'lumot olish yoki xizmatni bron qilish uchun biz bilan bog'laning!

Eng yaxshi ezgu tilaklar bilan, <code>Luxe Cleaning</code>
            """.format("Turi", "bir martalik", "oyiga 10-20", service_pr)

    else:  # Russian language version
        for ser in _service_:
            # Add service title
            service_pr += "<code>{:^}</code>\n".format(ser.title_ru)
            # service_pr += "{:<15} {:<32} {:<45}\n".format("Size", "Daily", "Monthly")

            # Accumulate prices per service
            for pr in TgServicesPrice.objects.filter(service=ser):
                service_pr += "{:<15} {:<25} {:<35}\n".format(
                    pr.size_ru, pr.daily_price_ru, pr.monthly_price_ru
                )
            service_pr += "\n"  # Add space between services

            # Final message with services list
        bot_msg = """
<b>Спасибо за интерес к нашим услугам!</b>

Услуги, которые мы предлагаем на данный момент:
<code>{:<4} {:<15} {:<25}</code>

{}
Свяжитесь с нами для получения дополнительной информации или заказа услуги!

С наилучшими пожеланиями, <code>Luxe Cleaning</code>
""".format("Тип", "одну уборку", "10-20 за месяц", service_pr)

    # Send the reply with the formatted services list
    update.message.reply_html(bot_msg, reply_markup=kb.back(user_db.lang))
    return state.GET_MENU
