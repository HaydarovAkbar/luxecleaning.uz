from typing import List
from enum import Enum
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
    def phone_number():
        keyboard = [KeyboardButton('Send contact', request_contact=True)]
        return ReplyKeyboardMarkup([keyboard], resize_keyboard=True)

    @staticmethod
    def location():
        keyboard = [KeyboardButton('Send location', request_location=True)]
        return ReplyKeyboardMarkup([keyboard], resize_keyboard=True)

    @staticmethod
    def base(lang: str):
        base_menu = msg().base_menu.get(lang)
        reply_buttons = []
        i = []
        for button in base_menu:
            i.append(button)
            if len(i) == 2:
                reply_buttons.append(i)
                i = []
        if i:
            reply_buttons.append(i)
        return ReplyKeyboardMarkup(reply_buttons, resize_keyboard=True)

    @staticmethod
    def back():
        reply_buttons = [
            ['⬅️ Orqaga']
        ]
        return ReplyKeyboardMarkup(reply_buttons, resize_keyboard=True)

    @staticmethod
    def youtube_file_size(file_size: List[int]):
        inline, i = [], 0
        result_size = []
        for size in file_size:
            result_size.append(str(round(size / 1024 / 1024, 2)) + ' MB')
        file_size = result_size
