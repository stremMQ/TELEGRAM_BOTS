import aiogram
import asyncio
import json
import requests
from bs4 import BeautifulSoup
from aiogram.filters import Command
from aiogram import Dispatcher, Bot, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
bot = Bot("")
dp = Dispatcher()

kurs = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = "курс")
        ]
    ]
)

async def bitoc(message: Message):
    response = requests.get(url)
    rez = response.json()
    await message.answer(f"курс {rez["symbol"]} = {rez["price"]} USDT")

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(f"Привет лох {message.from_user.first_name}", reply_markup = kurs)

@dp.message()
async def echo(message: Message):
    mes = message.text.lower()
    if mes == "курс":
        await bitoc(message)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
