import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery

from config import TOKEN
import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Пожалуйста, нажмите кнопку', reply_markup=kb.main)

@dp.message(F.text == 'Привет')
async def test_buton(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}')

@dp.message(F.text == 'Пока')
async def test_buton(message: Message):
    await message.answer(f'Пока, {message.from_user.first_name}')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())