from aiogram.types import KeyboardButton
from aiogram.types import ReplyKeyboardMarkup

b1 = KeyboardButton("/Lviv")
b2 = KeyboardButton("/Another_City")

keyboard_client = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_client.row(b1, b2)
