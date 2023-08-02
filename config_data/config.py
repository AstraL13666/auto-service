from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage


bot = Bot(token='6073449666:AAG5BAYJSSfnTZHANX4RzB0X1KjArEX-5ac')  # '5830183516:AAEJxq5EN-S93c5wEa3qnACtX0lDQHv2YRw'
dp = Dispatcher(storage=MemoryStorage())


class LinkID:
    def __init__(self):
        self.chat = -923973234  # -1001571427188
        self.channel = -1001902560054
        self.admins = 1192511915
