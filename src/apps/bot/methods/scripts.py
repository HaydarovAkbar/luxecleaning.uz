from .keyboards import Keyboards as kb
from .messages import Messages as msg
from telegram import Update, Bot
from telegram.ext import CallbackContext
from telegram import Update
from ..states import States as state


def start(update: Update, context: CallbackContext):
    update.message.reply_text(msg.start, reply_markup=kb.language())
    return state.START
