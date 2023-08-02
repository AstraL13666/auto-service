from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton


class Inline:

    def auto_center(self):
        b = InlineKeyboardBuilder()
        b.row(InlineKeyboardButton(text="Instagram", url="t.me/tests_auto_service_bot"))
        b.row(InlineKeyboardButton(text="VK", url="t.me/tests_auto_service_bot"))
        b.row(InlineKeyboardButton(text="YouTube", url="t.me/tests_auto_service_bot"))
        return b.as_markup()

    def history(self):
        b = InlineKeyboardBuilder()
        b.row(InlineKeyboardButton(text="История", callback_data="my history"))
        return b.as_markup()

    def back(self):
        b = InlineKeyboardBuilder()
        b.row(InlineKeyboardButton(text="Назад", callback_data="back"))
        return b.as_markup()
