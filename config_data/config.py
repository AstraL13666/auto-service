from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage


bot = Bot(token='5990241109:AAFCF5fvWCkWYc8JnV8tKK7GnSP-Y602A3I')
dp = Dispatcher(storage=MemoryStorage())
