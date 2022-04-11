from aiogram import Bot
from aiogram import Dispatcher
from aiogram import executor
from aiogram import types

from configs import api_config
from configs.keyboard import telegram_keyboard
from controller import weather_controller
from data.response.ErrorResponse import ErrorResponse
from data.response.WeatherResponse import WeatherResponse

TELEGRAM_TOKEN = api_config.get_telegram_token()

bot = Bot(token=TELEGRAM_TOKEN, parse_mode=types.ParseMode.HTML)
dispatcher = Dispatcher(bot)


@dispatcher.message_handler(commands=["start"])
async def start(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text="Hello!",
        reply_markup=telegram_keyboard.keyboard_client
    )


@dispatcher.message_handler(commands=["Lviv"])
async def get_weather_for_lviv(message: types.Message):
    weather_response = weather_controller.get_weather_data(city="lviv", imperial=False)

    if isinstance(weather_response, WeatherResponse):
        city = weather_response.name
        temperature = weather_response.temperature
        weather_symbol = weather_controller.select_weather_display_params(weather_response.id)

        await bot.send_message(
            chat_id=message.chat.id,
            text=f"<b>{city}</b>: {weather_symbol} {weather_response.description.capitalize()}, {temperature}°C",
            parse_mode=types.ParseMode.HTML
        )
    elif isinstance(weather_response, ErrorResponse):
        await bot.send_message(
            chat_id=message.chat.id,
            text=f"{weather_response.error_message}"
        )


async def on_startup(_):
    print("Bot is online")


executor.start_polling(dispatcher=dispatcher, on_startup=on_startup)
