import logging
from checkWord import checkword
from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = '5271825280:AAHDOqAUl5ISu_IlzaHnqG32RWh4mXeFG8g'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Imlo botimizga xush kelibsiz!!!")


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("Bu bot siz yozgan so'zlarni to'gri yoki tog'ri emasligini tekshirib beradi!!!")


@dp.message_handler()
async def checkimlo(message: types.Message):
    words = message.text.split()
    for word in words:
        result = checkword(word)
        if result['availible']:
            response = f"✅ {word.capitalize()}"
        else:
            response = f"❌ {word.capitalize()}\n"
            for text in result['matches']:
                response += f"✅ {text.capitalize()}\n"
        await message.reply(response)
    

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)