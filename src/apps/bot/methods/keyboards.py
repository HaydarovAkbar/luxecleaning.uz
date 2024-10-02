from typing import List
from enum import Enum
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


class Keyboards:
    def __init__(self):
        self._keyboards = {}

    @staticmethod
    def language():
        inline = [
            [
                InlineKeyboardButton('O\'zbek', callback_data='uz'),
                InlineKeyboardButton('Русский', callback_data='ru'),
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
    def base():
        reply_buttons = [
            ['📚 Kurslar', '📝 Testlar'],
            ['📊 Natijalar', '📞 Aloqa']
        ]
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
