from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext, \
    CallbackQueryHandler
from decouple import config
from django.conf import settings
from .methods.scripts import start, get_lang, help, services, about, contact, user_settings
from .methods.messages import Messages as msg
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
                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('ru')[0] + ')$'),
                                     services),
                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('ru')[1] + ')$'),
                                     about),
                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('ru')[2] + ')$'),
                                     contact),
                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('ru')[3] + ')$'),
                                     user_settings),

                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('uz')[0] + ')$'),
                                     services),
                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('uz')[1] + ')$'),
                                     about),
                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('uz')[2] + ')$'),
                                     contact),
                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('uz')[3] + ')$'),
                                     user_settings),
                      ],
    },
    fallbacks=[CommandHandler('start', start),
               CommandHandler('help', help), ]
)

dispatcher.add_handler(all_handler)
