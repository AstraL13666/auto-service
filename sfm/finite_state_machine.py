from aiogram.fsm.state import StatesGroup, State


class SignUp(StatesGroup):
    start = State()
    finish = State()


class Feedback(StatesGroup):
    wait = State()

    call_name = State()
    call_number = State()
    call_finish = State()

    feed = State()

    choice_name = State()
    choice_number = State()
    choice_finish = State()


