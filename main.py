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


@dp.message(Command('links'))
async def links(message: Message):
    await message.answer(f'Пожалуйста, нажмите кнопку ссылки', reply_markup=kb.inline_keyboard_links)


@dp.message(Command('dynamic'))
async def dynamic(message: Message):
    await message.answer(f'Пожалуйста, нажмите кнопку', reply_markup=kb.inline_keyboard_dynamic)

@dp.callback_query(F.data == 'show_more')
async def news(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(f'Показать больше', reply_markup=await kb.inline_keyboard_options())

@dp.callback_query(F.data == 'option_1')
async def news(callback: CallbackQuery):
    await callback.answer(f'Выбрана Опция 1', show_alert=True)

@dp.callback_query(F.data == 'option_2')
async def news(callback: CallbackQuery):
    await callback.answer(f'Выбрана Опция 2', show_alert=True)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())