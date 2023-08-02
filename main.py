import asyncio

from config_data import dp, bot
from handler import r, callback_router

from utils import setup_logger


async def polling_bot():

    setup_logger("INFO", ["sqlalchemy.engine", "aiogram.bot.api"])

    dp.include_routers(r, callback_router)

    try:
        await dp.start_polling(bot)

    except Exception as error:
        print(f'ERROR | {error}')

    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(polling_bot())
