from aiogram import Bot, Dispatcher, types
import asyncio

TOKEN = "ТОКЕН_ТВОЕГО_БОТА"
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(commands=["start"])
async def start(msg: types.Message):
    await msg.answer("👋 Привет! Я обменник крипты на рубли.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
