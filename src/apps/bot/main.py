from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext, \
    CallbackQueryHandler
from decouple import config
from django.conf import settings
# from .methods.base import start
# from .methods.admin import admin
import logging
from .states import States as state

# from .messages.main import KeyboardText as msg_text

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello!')


def send_feedback(update: Update, context: CallbackContext, data: dict):
    print(data)
    context.bot.send_message(chat_id=1683404154, text='Thank you for your message!')


def run():
    print('started webhook')
    bot.set_webhook(settings.HOST + '/Ikamezukashi/')


bot: Bot = Bot(token=config('TOKEN'))

dispatcher = Dispatcher(bot, None)

all_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start),
                  CommandHandler('help', help),
                  ],
    states={

    },
    fallbacks=[CommandHandler('start', start),
               CommandHandler('help', help),]
)

dispatcher.add_handler(all_handler)
