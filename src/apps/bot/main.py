from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext, \
    CallbackQueryHandler
from decouple import config
from django.conf import settings
from .methods.scripts import start, get_lang, help
# from .methods.admin import admin
import logging
from .states import States as st

# from .messages.main import KeyboardText as msg_text

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


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
        st.GET_LANG: [CallbackQueryHandler(get_lang)],
        st.GET_MENU: [CommandHandler('start', start),
                      CommandHandler('help', help),

                      ],
    },
    fallbacks=[CommandHandler('start', start),
               CommandHandler('help', help), ]
)

dispatcher.add_handler(all_handler)
