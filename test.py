import asyncio
import logging
import sys
from os import getenv
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from commands import reg_commands

# Настройка логирования (опционально, но полезно)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

TOKEN = "8093780985:AAG8OAE1xyl8R68OXSpYq4IutALWXbtdEp0"

# 2. Создаём диспетчер
dp = Dispatcher()

reg_commands(dp)

async def main() -> None:
    # Создаём экземпляр Bot с HTML-парсингом
    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    # 5.2 Запускаем polling
    await dp.start_polling(bot)  # :contentReference[oaicite:9]{index=9}

# 6. Точка входа
if __name__ == "__main__":
    asyncio.run(main())  # :contentReference[oaicite:10]{index=10}