import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot("7957065214:AAGxFxVtTByCSzMpFjBQt3joaXuhPTqnzzk")
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Бот работает 24/7 🚀")

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
