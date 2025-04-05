import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from fastapi import FastAPI


TOKEN = "8054015931:AAH4GAxOTCnCLCyrwtW28f05KQl48eYnjkA"
bot = Bot(token=TOKEN)
dp = Dispatcher()



@dp.message(CommandStart)
async def command_start(message: Message) -> None:
    await message.answer("Привет")



async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())