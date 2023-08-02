import asyncio

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters.command import Command

from aiogram.fsm.context import FSMContext

from config_data import bot
from dataclass import data_sign_up, data_feedback
from keyboard import kbrd
from sfm import SignUp, Feedback
from utils import txt

r = Router(name="router chat")


@r.message(Command("start"))
async def command_start(m: Message):
    await m.answer(
        text='Test AutoService - автосервис для Вас',
        reply_markup=kbrd.button.menu()
    )


@r.message(F.text == "Автоцентр")
async def auto_center(m: Message):
    await m.answer(
        text=txt.auto_service,
        reply_markup=kbrd.inline.auto_center(),
        parse_mode="HTML"
    )


# TODO Выборка из базы свободных мест на ремонт
@r.message(F.text == "Записаться")
async def sign_up(m: Message, state: FSMContext):
    await m.answer(
        text=txt.sign_up,
        reply_markup=kbrd.button.sign_up(),
        parse_mode="HTML"
    )

    await state.set_state(SignUp.start)


@r.message(SignUp.start, F.text.in_(txt.services))
async def sign_up_start(m: Message, state: FSMContext):
    await m.answer(
        text=txt.sign_up_start(value=m.text),
        parse_mode="HTML"
    )

    data_sign_up.serv = {'title': m.text}

    await state.set_state(SignUp.finish)


@r.message(SignUp.finish)
async def sign_up_finish(m: Message, state: FSMContext):
    data_sign_up.serv['problem'] = m.text

    await m.answer(
        text=txt.sign_up_finish(value=data_sign_up.serv),
        parse_mode="HTML"
    )
    await asyncio.sleep(2)
    await m.answer(
        text="Спасибо за обращение, открыл главное меню",
        reply_markup=kbrd.button.menu(),
    )

    await state.clear()


@r.message(F.text == "Обратная связь")
async def feed_back(m: Message, state: FSMContext):
    await m.answer(
        text=txt.calls,
        reply_markup=kbrd.button.feedback(),
        parse_mode="HTML"
    )
    await state.set_state(Feedback.wait)


@r.message(Feedback.wait, F.text.in_(txt.call_quest))
async def feed_back_choice(m: Message, state: FSMContext):
    if m.text == txt.call_quest[-1]:
        # Меню
        await state.clear()
        await m.answer(
            text="Меню",
            reply_markup=kbrd.button.menu()
        )

    else:
        if m.text == txt.call_quest[0]:

            # Звонок
            await m.answer(
                text="1) Как Вас зовут?",
                reply_markup=ReplyKeyboardRemove()
            )
            await state.set_state(Feedback.call_name)

        elif m.text == txt.call_quest[1]:
            # Отзыв
            await m.answer(
                text=txt.feedback,
                reply_markup=ReplyKeyboardRemove(),
                parse_mode="HTML"
            )
            await state.set_state(Feedback.feed)

        else:
            # Задать вопрос
            await m.answer(
                text="1) Как Вас зовут?",
                reply_markup=ReplyKeyboardRemove()
            )
            await state.set_state(Feedback.choice_name)


# звонок
@r.message(Feedback.call_name)
async def fb_call_name(m: Message, state: FSMContext):
    data_feedback.temp = {"name": m.text}
    await m.answer(
        text="2) Введите Ваш номер телефона:\n\nПожалуйста, указывайте только актуальный номер телефона"
    )
    await state.set_state(Feedback.call_number)


@r.message(Feedback.call_number)
async def fb_call_number(m: Message, state: FSMContext):
    data_feedback.temp["number"] = m.text
    await m.answer(
        text="3) Укажите удобное время для связи:",
        reply_markup=kbrd.button.time_call()
    )
    await state.set_state(Feedback.call_finish)


@r.message(Feedback.call_finish)
async def fb_call_finish(m: Message, state: FSMContext):
    data_feedback.temp["time"] = m.text

    await asyncio.sleep(0.2)
    await m.answer(
        text=txt.call(value=data_feedback.temp),
        parse_mode="HTML"
    )

    data_feedback.temp.clear()

    await state.clear()
    await asyncio.sleep(0.5)
    await m.answer(
        text="Меню",
        reply_markup=kbrd.button.menu()
    )


# feedback
@r.message(Feedback.feed)
async def fb_feedback(m: Message, state: FSMContext):
    data_feedback.temp = {'feed': m.text}

    await m.answer(
        text=txt.send_fb(value=data_feedback.temp),
        reply_markup=kbrd.button.menu(),
        parse_mode="HTML"
    )

    data_feedback.temp.clear()
    await state.clear()
    await asyncio.sleep(0.2)


# вопрос
@r.message(Feedback.choice_name)
async def c_number(m: Message, state: FSMContext):
    data_feedback.temp = {"name": m.text}
    await m.answer(
        text="2) Напишите Ваш номер телефона:"
    )
    await state.set_state(Feedback.choice_number)


@r.message(Feedback.choice_number)
async def c_choice_finish(m: Message, state: FSMContext):
    data_feedback.temp["number"] = m.text
    await m.answer(
        text="Напишите Ваш вопрос:"
    )
    await state.set_state(Feedback.choice_finish)


@r.message(Feedback.choice_finish)
async def choice_finish(m: Message, state: FSMContext):
    data_feedback.temp["choice"] = m.text

    await m.answer(
        text=txt.send_choice(value=data_feedback.temp),
        reply_markup=kbrd.button.menu(),
        parse_mode="HTML"
    )
    await asyncio.sleep(0.1)
    data_feedback.temp.clear()
    await state.clear()


@r.message(F.text == "Маршрут")
async def route(m: Message):
    await m.answer(
        text=txt.route,
        parse_mode="HTML"
    )
    await bot.send_venue(
        chat_id=m.chat.id,
        latitude=txt.address_lat,
        longitude=txt.address_lon,
        title="Google Maps",
        address=txt.address
    )


@r.message(F.text == "Профиль")
async def profile(m: Message):
    await m.answer(
        text=txt.profile(value=m),
        reply_markup=kbrd.inline.history(),
        parse_mode="HTML"
    )
