import Config
import asyncio
import logging
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(Config.TOKEN)
# Диспетчер
dp = Dispatcher()

# Пулы сообщений для каждой кнопки
pool1 = ["Message 1", "Message 2", "Message 3"]
pool2 = ["Message A", "Message B", "Message C"]
pool3 = ["Message X", "Message Y", "Message Z"]
pool4 = ["Random 1", "Random 2", "Random 3"]


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Button 1")
    button2 = types.KeyboardButton("Button 2")
    button3 = types.KeyboardButton("Button 3")
    button4 = types.KeyboardButton("Button 4")
    keyboard.add(button1, button2, button3, button4)

    await message.answer("Hello!", reply_markup=keyboard)


# Обработчики для кнопок
@dp.message(lambda message: message.text == "Button 1")
async def button1_handler(message: types.Message):
    await message.answer(random.choice(pool1))


@dp.message(lambda message: message.text == "Button 2")
async def button2_handler(message: types.Message):
    await message.answer(random.choice(pool2))


@dp.message(lambda message: message.text == "Button 3")
async def button3_handler(message: types.Message):
    await message.answer(random.choice(pool3))


@dp.message(lambda message: message.text == "Button 4")
async def button4_handler(message: types.Message):
    await message.answer(random.choice(pool4))


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
