from .keyboards import Keyboards as kb
from .messages import Messages as msg
from telegram import Update, Bot
from telegram.ext import CallbackContext
from telegram import Update
from ..states import States as state
from apps.models import TgUsers


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


def help(update: Update, context: CallbackContext):
    update.message.reply_text(msg().help.get(update.message.from_user.language_code))
    return state.START
