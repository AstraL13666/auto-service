from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage


bot = Bot(token='pass')
dp = Dispatcher(storage=MemoryStorage())
