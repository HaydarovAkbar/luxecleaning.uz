from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext, \
    CallbackQueryHandler
from telegram.error import RetryAfter
import time
from decouple import config
from django.conf import settings
from .methods.scripts import start, get_lang, help, services, contact, user_settings, change_lang, \
    corporate_clients, get_corporate_phone, corporative_client_msg, discount, faq_and_connection, service_and_price, \
    change_phone_number, get_full_name, get_name, get_video, message, connection_with_admin, get_service_type, re_phone, \
    my_orders
from .methods.messages import Messages as msg
import logging
from .states import States as st

# from .messages.main import KeyboardText as msg_text

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def run():
    webhook_url = settings.HOST + '/Ikamezukashi/'

    try:
        bot.set_webhook(webhook_url)
    except RetryAfter as e:
        print(f"Flood control exceeded. Retrying in {e.retry_after} seconds...")
        time.sleep(e.retry_after)  # Wait for the retry period
        bot.set_webhook(webhook_url)  # Try setting the webhook again

bot: Bot = Bot(token=config('TOKEN'))

dispatcher = Dispatcher(bot, None)

all_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start),
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
                                 service_and_price),
                  MessageHandler(Filters.regex('^(' + msg().base_menu.get('ru')[3] + ')$'),
                                 discount),
                  MessageHandler(Filters.regex('^(' + msg().base_menu.get('ru')[4] + ')$'),
                                 faq_and_connection),
                  MessageHandler(Filters.regex('^(' + msg().base_menu.get('ru')[5] + ')$'),
                                 contact),
                  MessageHandler(Filters.regex('^(' + msg().base_menu.get('ru')[6] + ')$'),
                                 my_orders),
                  MessageHandler(Filters.regex('^(' + msg().base_menu.get('ru')[7] + ')$'),
                                 user_settings),
                  MessageHandler(Filters.regex('^(' + msg().base_menu.get('ru')[8] + ')$'),
                                 connection_with_admin),

                  MessageHandler(Filters.regex('^(' + msg().base_menu.get('uz')[0] + ')$'),
                                 services),
                  MessageHandler(Filters.regex('^(' + msg().base_menu.get('uz')[1] + ')$'),
                                 corporate_clients),
                  MessageHandler(Filters.regex('^(' + msg().base_menu.get('uz')[2] + ')$'),
                                 service_and_price),
                  MessageHandler(Filters.regex('^(' + msg().base_menu.get('uz')[3] + ')$'),
                                 discount),
                  MessageHandler(Filters.regex('^(' + msg().base_menu.get('uz')[4] + ')$'),
                                 faq_and_connection),
                  MessageHandler(Filters.regex('^(' + msg().base_menu.get('uz')[5] + ')$'),
                                 contact),
                  MessageHandler(Filters.regex('^(' + msg().base_menu.get('uz')[6] + ')$'),
                                 my_orders),
                  MessageHandler(Filters.regex('^(' + msg().base_menu.get('uz')[7] + ')$'),
                                 user_settings),
                  MessageHandler(Filters.regex('^(' + msg().base_menu.get('uz')[8] + ')$'),
                                 connection_with_admin),
                  MessageHandler(Filters.all, start),
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
                                     service_and_price),
                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('ru')[3] + ')$'),
                                     discount),
                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('ru')[4] + ')$'),
                                     faq_and_connection),
                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('ru')[5] + ')$'),
                                     contact),
                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('ru')[6] + ')$'),
                                     my_orders),
                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('ru')[7] + ')$'),
                                     user_settings),
                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('ru')[8] + ')$'),
                                     connection_with_admin),

                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('uz')[0] + ')$'),
                                     services),
                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('uz')[1] + ')$'),
                                     corporate_clients),
                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('uz')[2] + ')$'),
                                     service_and_price),
                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('uz')[3] + ')$'),
                                     discount),
                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('uz')[4] + ')$'),
                                     faq_and_connection),
                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('uz')[5] + ')$'),
                                     contact),
                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('uz')[6] + ')$'),
                                     my_orders),
                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('uz')[7] + ')$'),
                                     user_settings),
                      MessageHandler(Filters.regex('^(' + msg().base_menu.get('uz')[8] + ')$'),
                                     connection_with_admin),
                      MessageHandler(Filters.all, start),
                      ],
        st.CORPORATE_CLIENTS: [
            CommandHandler('start', start),
            CommandHandler('help', help),
            MessageHandler(Filters.regex('^(' + msg().back.get('ru') + ')$'), start),
            MessageHandler(Filters.regex('^(' + msg().back.get('uz') + ')$'), start),
            MessageHandler(Filters.contact, get_corporate_phone),
            MessageHandler(Filters.text, corporative_client_msg),
        ],
        # st.SERVICE: [
        #     CommandHandler('start', start),
        #     CommandHandler('help', help),
        #     MessageHandler(Filters.regex('^(' + msg().back.get('ru') + ')$'), start),
        #     MessageHandler(Filters.regex('^(' + msg().back.get('uz') + ')$'), start),
        #     MessageHandler(Filters.text, use_of_service),
        # ],
        st.GET_SERVICE_TYPE: [
            CommandHandler('start', start),
            CommandHandler('help', help),
            CallbackQueryHandler(get_service_type)
        ],
        st.GET_PHONE_NUMBER: [
            CommandHandler('start', start),
            CommandHandler('help', help),
            MessageHandler(Filters.regex('^(' + msg().back.get('ru') + ')$'), start),
            MessageHandler(Filters.regex('^(' + msg().back.get('uz') + ')$'), start),
            MessageHandler(Filters.regex('^(' + msg().continiue_msg.get('ru') + ')$'), get_full_name),
            MessageHandler(Filters.regex('^(' + msg().continiue_msg.get('uz') + ')$'), get_full_name),
            MessageHandler(Filters.contact, change_phone_number),
            MessageHandler(Filters.text, re_phone),
        ],
        st.GET_NAME: [
            CommandHandler('start', start),
            CommandHandler('help', help),
            MessageHandler(Filters.regex('^(' + msg().back.get('ru') + ')$'), start),
            MessageHandler(Filters.regex('^(' + msg().back.get('uz') + ')$'), start),
            MessageHandler(Filters.text, get_name),
        ],
        st.GET_VIDEO: [
            CommandHandler('start', start),
            CommandHandler('help', help),
            MessageHandler(Filters.regex('^(' + msg().back.get('ru') + ')$'), start),
            MessageHandler(Filters.regex('^(' + msg().back.get('uz') + ')$'), start),
            MessageHandler(Filters.all, get_video),
        ],
        st.MESSAGE: [
            CommandHandler('start', start),
            CommandHandler('help', help),
            MessageHandler(Filters.regex('^(' + msg().back.get('ru') + ')$'), start),
            MessageHandler(Filters.regex('^(' + msg().back.get('uz') + ')$'), start),
            MessageHandler(Filters.all, message)
        ],
    },
    fallbacks=[CommandHandler('start', start),
               CommandHandler('help', help), ]
)

dispatcher.add_handler(all_handler)
