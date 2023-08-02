from aiogram.types import Message
from aiogram.filters.command import CommandStart


async def command_start(m: Message):
    await m.answer(
        text='Hi'
    )


def register_message_handlers(dp):
    dp.message.register(command_start, CommandStart())
