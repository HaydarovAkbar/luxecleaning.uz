from typing import List
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from .messages import Messages as msg


class Keyboards:
    def __init__(self):
        self._keyboards = {}

    @staticmethod
    def language():
        inline = [
            [
                InlineKeyboardButton('O\'zbek 🇺🇿', callback_data='uz'),
                InlineKeyboardButton('Русский 🇷🇺', callback_data='ru'),
                # InlineKeyboardButton('English', callback_data='en')
            ]
        ]
        return InlineKeyboardMarkup(inline)

    @staticmethod
    def phone_number(lang: str):
        kb_txt = msg().send_phone_keyb.get(lang)
        back_txt = msg().back.get(lang)
        keyboard = [KeyboardButton(kb_txt, request_contact=True)]
        return ReplyKeyboardMarkup([keyboard, [back_txt]], resize_keyboard=True)
        # return ReplyKeyboardMarkup([keyboard], resize_keyboard=True)

    @staticmethod
    def location():
        keyboard = [KeyboardButton('Send location', request_location=True)]
        return ReplyKeyboardMarkup([keyboard], resize_keyboard=True)

    @staticmethod
    def base(lang: str):
        base_menu = msg().base_menu.get(lang)
        reply_buttons = [
            [base_menu[0]],
            [base_menu[1]],
            [base_menu[2], base_menu[3]],
            [base_menu[4], base_menu[5]],
            [base_menu[6]],
            [base_menu[7]]
        ]
        return ReplyKeyboardMarkup(reply_buttons, resize_keyboard=True)

    @staticmethod
    def back(lang: str):
        back_txt = msg().back.get(lang)
        reply_buttons = [
            [back_txt]
        ]
        return ReplyKeyboardMarkup(reply_buttons, resize_keyboard=True)
