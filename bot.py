import logging
from aiogram import Bot, Dispatcher, types
from config import YOU_TELEGRAM_TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(YOU_TELEGRAM_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.chat.id, 'Privet Durachok')

