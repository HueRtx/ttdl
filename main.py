import yt_dlp
import asyncio
import logging
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = "6277867049:AAFzx3QuWnCDFnwQUHzEn4DQaO0JoVvWMZM"
# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! 👋 Я бот для скачивания видео и звуков с TikTok. 🎵🎥 Напиши мне ссылку на видео, и я помогу тебе скачать его. 📥")

@router.message()
async def echo_handler(message: types.Message) -> None:
    try:
        if message.text.startswith('https://'):
            await message.answer("Выбери что тебе надо скачать", builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="Видео",
            callback_data="video")
            ))

    except TypeError:
        await message.answer("Хорошая попытка")


# Запуск процесса поллинга новых апдейтов
async def main() -> None:
    # Dispatcher is a root router
    dp = Dispatcher()
    # ... and all other routers should be attached to Dispatcher
    dp.include_router(router)

    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode="HTML")
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())