from aiogram import Router, F
from aiogram.handlers.callback_query import CallbackQuery

from config_data import bot
from keyboard import kbrd
from utils import txt


callback_router = Router(name='callback_router')


@callback_router.callback_query(F.data == 'my history')
async def history_back(call: CallbackQuery):
    await bot.edit_message_text(
        text=txt.history,
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=kbrd.inline.back(),
        parse_mode="HTML"
    )


@callback_router.callback_query(F.data == 'back')
async def history_back(call: CallbackQuery):
    await bot.edit_message_text(
        text=txt.profile(value=call),
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=kbrd.inline.history(),
        parse_mode="HTML"
    )



