from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Привет')],
    [KeyboardButton(text='Пока')]
], resize_keyboard=True)


inline_keyboard_links = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Новости', url='https://www.kinoafisha.info/person/7791245/news/')],
    [InlineKeyboardButton(text='Музыка', url='https://my.mail.ru/music/search/%D0%AD%D0%BD%D1%82%D0%BE%D0%BD%D0%B8%20%D0%A5%D0%BE%D0%BF%D0%BA%D0%B8%D0%BD%D1%81%20%D0%B8%20%D0%B5%D0%B3%D0%BE%20%D0%B2%D0%BE%D0%BB%D1%88%D0%B5%D0%B1%D0%BD%D1%8B%D0%B9%20%D0%B2%D0%B0%D0%BB%D1%8C%D1%81')],
    [InlineKeyboardButton(text='Видео', url='https://vk.com/video-139058943_456239185')]
])


inline_keyboard_dynamic = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Показать больше', callback_data='show_more')]
])

async def inline_keyboard_options():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Опция 1', callback_data='option_1'))
    keyboard.add(InlineKeyboardButton(text='Опция 2', callback_data='option_2'))
    return keyboard.adjust(2).as_markup()