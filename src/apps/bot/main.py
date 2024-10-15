from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext, \
    CallbackQueryHandler
from decouple import config
from django.conf import settings
from .methods.scripts import start, get_lang, help, services, about, contact, user_settings, change_lang, \
    corporate_clients, get_corporate_phone, corporative_client_msg, discount, faq_and_connection
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
        st.GET_LANG: [CommandHandler('start', start), CallbackQueryHandler(get_lang)],
        st.CHANGE_LANG: [CommandHandler('start', start), CallbackQueryHandler(change_lang)],
        st.GET_MENU: [CommandHandler('start', start),
                      CommandHandler('help', help),

                      MessageHandler(Filters.regex('^(' + msg().back.get('ru') + ')$'),
                                     start),
                      MessageHandler(Filters.regex('^(' + msg().back.get('uz') + ')$'),
                                     start),

                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('ru')[0] + ')$'),
                                     services),
                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('ru')[1] + ')$'),
                                     corporate_clients),
                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('ru')[2] + ')$'),
                                     discount),
                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('ru')[3] + ')$'),
                                     discount),
                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('ru')[4] + ')$'),
                                     faq_and_connection),
                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('ru')[5] + ')$'),
                                     contact),
                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('ru')[6] + ')$'),
                                     contact),
                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('ru')[7] + ')$'),
                                     user_settings),

                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('uz')[0] + ')$'),
                                     services),
                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('uz')[1] + ')$'),
                                     corporate_clients),
                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('uz')[2] + ')$'),
                                     discount),
                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('uz')[3] + ')$'),
                                     discount),
                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('uz')[4] + ')$'),
                                     faq_and_connection),
                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('uz')[5] + ')$'),
                                     contact),
                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('uz')[6] + ')$'),
                                     contact),
                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('uz')[7] + ')$'),
                                     user_settings),
                      ],
        st.CORPORATE_CLIENTS: [
            CommandHandler('start', start),
            CommandHandler('help', help),
            MessageHandler(Filters.regex('^(' + msg().back.get('ru') + ')$'), start),
            MessageHandler(Filters.regex('^(' + msg().back.get('uz') + ')$'), start),
            MessageHandler(Filters.contact, get_corporate_phone),
            MessageHandler(Filters.text, corporative_client_msg),
        ],

    },
    fallbacks=[CommandHandler('start', start),
               CommandHandler('help', help), ]
)

dispatcher.add_handler(all_handler)
