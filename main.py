import asyncio
import logging
import yt_dlp
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
import random


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! 👋 Я бот для скачивания видео и звуков с TikTok. 🎵🎥 Напиши мне ссылку на видео, и я помогу тебе скачать его. 📥")

@dp.message()
async def vid_n_sound(message: types.Message):
    filename = random.randint(1,99999) 
    filename_aud = random.randint(1,99999)
    ydl_opts = {
        'outtmpl': f"/home/floduat/bot/{filename}.mp4",
    }
    ydl_opts_aud = {
    'format': 'bestaudio/best',
    'outtmpl': f"/home/floduat/bot/{filename_aud}",
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([message.text])
    with yt_dlp.YoutubeDL(ydl_opts_aud) as ydl:
        ydl.download([message.text])
    await bot.send_audio(message.from_user.id, types.FSInputFile(f"{filename_aud}.mp3"))
    await bot.send_video(message.from_user.id, types.FSInputFile(f"{filename}.mp4"))

#@dp.message()
#async def otvet1(message: types.Message) -> None:
#    builder = InlineKeyboardBuilder()
#    builder.add(types.InlineKeyboardButton(
#        text="Видео🎥",
#        callback_data="vid"), types.InlineKeyboardButton(
#        text="Звук🎵",
#        callback_data="song"))
#    await message.answer(text="Выбери что хочешь загрузить", reply_markup=builder.as_markup())
#@dp.callback_query(Text("vid"))
#async def send_vid(callback: types.CallbackQuery,message: types.Message):
#    ydl_opts = {}
#    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#        ydl.download([message.text])
#    await callback.message.answer_photo

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())