import asyncio
from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from fastapi import FastAPI, Query
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import uvicorn
from typing import List, Optional
import json

TOKEN = "8054015931:AAH4GAxOTCnCLCyrwtW28f05KQl48eYnjkA"
bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()
app=FastAPI()
dp.include_router(router)

mainKeyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Список номеров")],
    [KeyboardButton(text="Запись на номер")],
    [KeyboardButton(text="Данные о времени для записи")],
    [KeyboardButton(text="Список распределенных номеров")],
], resize_keyboard=True)

numbers = ['1', '2', '3']

async def inline_numbers():
    keyboard = ReplyKeyboardBuilder()
    for number in numbers:
        keyboard.add(KeyboardButton(text=number))
    keyboard.add(KeyboardButton(text="Назад"))  
    return keyboard.adjust(2).as_markup()

class NumberRecord(StatesGroup):
    waiting_for_number = State()
    show_numbers = State() 

@router.message(CommandStart())
async def command_start(message: Message) -> None:
    await message.answer("Привет", reply_markup=mainKeyboard)

@router.message(F.text == "Список номеров")#не доконца норм работает
async def list_numbers(message: Message, state: FSMContext) -> None:
    await get_numbers()
    await message.answer("Доступные номера:")
    print(numbers)
   # for number in numbers:
     #   await message.answer(number)
    await state.set_state(NumberRecord.show_numbers) 

@router.message(NumberRecord.show_numbers, F.text == "Назад") 
async def back_to_main_menu_from_numbers(message: Message, state: FSMContext) -> None:
    await message.answer("Возвращаемся в главное меню", reply_markup=mainKeyboard)
    await state.clear()

@router.message(F.text == "Запись на номер")
async def record_number(message: Message, state: FSMContext) -> None:
    await message.answer("Выберите номер для записи:", reply_markup=await inline_numbers())
    await state.set_state(NumberRecord.waiting_for_number)

@router.message(NumberRecord.waiting_for_number)
async def process_number_record(message: Message, state: FSMContext) -> None:
    if message.text in numbers:
        await message.answer(f"Вы записаны на номер {message.text}.")
        await state.clear()
    elif message.text == "Назад":
        await message.answer("Возвращаемся в главное меню", reply_markup=mainKeyboard)
        await state.clear()
    else:
        await message.answer("Пожалуйста, выберите номер из списка.")

@router.message(F.text == "Данные о времени для записи")
async def record_time(message: Message) -> None:
    await message.answer("Данные о времени для записи: ...")

@router.message(F.text == "Список распределенных номеров")
async def distributed_numbers(message: Message) -> None:
    await message.answer("Список распределенных номеров: ...")

@app.get("/problems")#не доконца норм работает
async def get_numbers(problems: Optional[str] = Query(None)):
    global numbers
    if problems is not None:
        try:
            numbers = json.loads(problems)
            return {"message": "Данные успешно получены", "numbers": numbers}
        except json.JSONDecodeError:
            return {"message": "Неправильный формат JSON", "numbers": []}
    else:
        return {"message": "Данные не были переданы", "numbers": []}

app.post("/assign")
async def set_user_number():
    pass

app.get("/info")
async def get_info():
    pass

app.get("/list")
async def get_users_list():
    pass

async def main():
    await dp.start_polling(bot)

async def start_bot():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        task_bot = loop.create_task(start_bot())
        config = uvicorn.Config(app, host="localhost", port=3000)
        server = uvicorn.Server(config=config)
        task_server = loop.create_task(server.serve())
        loop.run_until_complete(asyncio.gather(task_bot, task_server))

    except KeyboardInterrupt:
        pass
    finally:
        loop.close()