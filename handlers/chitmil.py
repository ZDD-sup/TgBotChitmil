from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.filters import Command
from states import ChitmilStates
from db.crud import save_chitmil_data


router = Router()

@router.message(Command("chitmil"), state=default_state)
async def start_chitmil(message: types.Message, state: FSMContext):
    await message.answer("Что ты хочешь себе разрешить сегодня?")
    await state.set_state(ChitmilStates.what_allow)

@router.message(ChitmilStates.what_allow)
async def get_what_allow(message: types.Message, state: FSMContext):
    await state.update_data(what_allow=message.text)
    await message.answer("Как назовём этот день?")
    await state.set_state(ChitmilStates.day_name)

@router.message(ChitmilStates.day_name)
async def get_day_name(message: types.Message, state: FSMContext):
    await state.update_data(day_name=message.text)
    await message.answer("На какой период? (в днях)")
    await state.set_state(ChitmilStates.period)

@router.message(ChitmilStates.period)
async def get_period(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Введите число.")
        return
    await state.update_data(period=int(message.text))
    await message.answer("Хочешь ли, чтобы период увеличивался со временем? (да/нет)")
    await state.set_state(ChitmilStates.increase)

@router.message(ChitmilStates.increase)
async def get_increase(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    increase = message.text.lower() in ["да", "yes", "y"]
    user_data["increase"] = increase

    summary = (
        f"📋 Вот что ты выбрал:\n"
        f"— Разрешить: {user_data['what_allow']}\n"
        f"— Название дня: {user_data['day_name']}\n"
        f"— Период: {user_data['period']} дней\n"
        f"— Увеличивать период: {'Да' if increase else 'Нет'}"
    )
    await save_chitmil_data(message.from_user.id, user_data)
    await message.answer(summary)
    await state.clear()

@router.message(Command("my_chitmils"))
async def show_user_chitmils(message: types.Message):
    from db.crud import get_user_chitmils

    entries = await get_user_chitmils(message.from_user.id)

    if not entries:
        await message.answer("У тебя пока нет записей.")
        return

    text = "📋 Твои Chitmil записи:\n\n"
    for entry in entries:
        text += (
            f"🗓 {entry.day_name} — {entry.what_allow}\n"
            f"⏳ Период: {entry.period} дней\n"
            f"🔁 Увеличение: {'Да' if entry.increase else 'Нет'}\n\n"
        )

    await message.answer(text.strip())