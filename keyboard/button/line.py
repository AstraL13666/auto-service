from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from utils import txt


class Button:

    def menu(self):
        kb = [
            [
                KeyboardButton(text="Автоцентр"),
                KeyboardButton(text="Записаться"),

            ],
            [
                KeyboardButton(text="Обратная связь"),
                KeyboardButton(text="Маршрут")
            ],
            [
                KeyboardButton(text="Профиль")
            ]
        ]
        return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

    def sign_up(self):
        kb = ReplyKeyboardBuilder()

        for _ in range(len(txt.services)):
            kb.add(KeyboardButton(text=txt.services[_]))
        kb.adjust(2)
        return kb.as_markup(resize_keyboard=True)

    def feedback(self):
        kb = ReplyKeyboardBuilder()

        for _ in range(len(txt.call_quest)):
            kb.add(KeyboardButton(text=txt.call_quest[_]))
        kb.adjust(2)
        return kb.as_markup(resize_keyboard=True)

    def time_call(self):
        kb = ReplyKeyboardBuilder()

        for _ in range(len(txt.time_call)):
            kb.add(KeyboardButton(text=txt.time_call[_]))
        kb.adjust(3)
        return kb.as_markup(resize_keyboard=True)
