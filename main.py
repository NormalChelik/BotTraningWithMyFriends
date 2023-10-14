from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

from handlers import router

token = open("token.txt").readline()

async def main() -> None:
    bot = Bot(token=token, parse_mode="Markdown")
    dp = Dispatcher(storage=MemoryStorage()) # ну здесь тоже все понятно блять
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True) # Игнорирование сообшений до запуска бота вот
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types()) # Запуск бота

if __name__ == '__main__':
    asyncio.run(main()) #Запускаем main что не понятно то

"""
- создать callback клаву под сообщением которое выводится при команде /start  
- в этих кнопках должны быть все спарсенные курсы валют 
"""