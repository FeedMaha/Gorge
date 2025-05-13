from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram import F
from aiogram.filters import Command, CommandStart
from aiogram import Dispatcher
import requests
from aiogram import types
from aiohttp import ClientSession
from bs4 import BeautifulSoup


def reg_commands(dp: Dispatcher):

    API_KEY = "0c348b36f19f46f89e6400e5682792f3"

    WORLDOMETERS_URL = "https://www.worldometers.info/world-population/india-population/"

    async def fetch_population_stats() -> tuple[int, int]:
        """
        Парсит страницу Worldometers и возвращает:
        births — количество рождений сегодня,
        deaths — количество смертей сегодня.
        """
        async with ClientSession() as session:
            async with session.get(WORLDOMETERS_URL) as resp:
                html = await resp.text()
        soup = BeautifulSoup(html, "html.parser")
        # Получаем текст внутри <span id="birthsToday">
        births = int(soup.find("span", {"id": "birthsToday"}).text.replace(",", ""))  # число рождений :contentReference[oaicite:4]{index=4}
        # Получаем текст внутри <span id="deathsToday">
        deaths = int(soup.find("span", {"id": "deathsToday"}).text.replace(",", ""))  # число смертей :contentReference[oaicite:5]{index=5}
        return births, deaths

    # логика активации
    async def do_nigga_sequence(message: Message):
        await message.answer(f"Nigga Link in the network")
        await message.answer(f"Activating the fentanyl reactor")
        await message.answer(f"Fentanyl reactor at full power")
        await message.answer(f"Downloading Microsoft Nigga AI")
        await message.answer(f"Fentanyl level 50%")
        await message.answer(f"Fentanyl level is 70%")
        await message.answer(f"Fentanyl level is 100% ....")
        await message.answer(f"Connecting to Niggatrix servers")
        await message.answer(f"Uploading to HitlerPorn.com")

    # клавиатура
    def get_inline_menu():
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="📰 Nigga News", callback_data="nigga_news")],
            [InlineKeyboardButton(text="😊 Good News", callback_data="good_news")],
            [InlineKeyboardButton(text="😞 Bad News", callback_data="bad_news")],
        ])
        return keyboard

    # новости
    def get_news():
        url = (
            f"https://newsapi.org/v2/everything?"
            f"q=technology&"
            f"sortBy=publishedAt&"
            f"language=en&"
            f"pageSize=5&"
            f"apiKey={API_KEY}"
        )
        response = requests.get(url)
        data = response.json()

        if data.get("status") != "ok":
            return "❌ Ошибка при получении новостей."

        articles = data.get("articles", [])
        if not articles:
            return "⚠️ Новости не найдены."

        news_list = []
        for article in articles[:10]:
            title = article.get("title", "Без заголовка")
            url = article.get("url", "")
            news_list.append(f"📰 <b>{title}</b>\n🔗 {url}")

        return "\n\n".join(news_list)

    # /start
    @dp.message(CommandStart())
    async def command_start_handler(message: Message) -> None:
        await do_nigga_sequence(message)

    # /nigga_link
    @dp.message(Command("nigga_link"))
    async def command_start_handler(message: Message) -> None:
        await message.answer(f"Joining to NiggaLink ...")
        await message.answer(f"Niggalink Activated: Fentanyl Production Increase by 25%/50%/70%/100%/ Protocol BlockChain Layer3 Engaged")
        await message.answer(f"Initiating Thermodynamic Bag Chaser 1 Gorillion TPS...")
        await message.answer(f"Engaging LLM Lil Lotta System Technology...")
        await message.answer(f"Decrypting databases for proof of nigga entry scan system...")
        await message.answer(f"Synthesizing Broke Nigga Detection(BND) Software...")
        await message.answer("Commands :", reply_markup=get_inline_menu())

    # /thanks
    @dp.message(Command("thanks"))
    async def command_thanks_handler(message: Message):
        await message.answer_animation(
            animation="https://i.imgur.com/lgjrNQk.gif",
            caption="No problem my nigga"
        )

    # /nigga_news
    @dp.message(Command("nigga_news"))
    async def send_news(message: types.Message):
        await message.answer(f"Data analysis complete. Presenting insights derived from current information below as requested:")
        await message.reply("Niggalink, access the internet and provide me data regarding the criminal activities of black communities in the hoods")
        news = get_news()
        await message.answer(news, parse_mode="HTML")

    # /good_news
    @dp.message(Command("good_news"))
    async def command_good_news_handler(message: Message) -> None:
        await message.answer(f"You a nigga")
        _, deaths = await fetch_population_stats()
        await message.answer(f"⚰️ Сегодня в Индии умерло: {deaths}")

    # /bad_news
    @dp.message(Command("bad_news"))
    async def command_bad_news_handler(message: Message) -> None:
        await message.answer(f"You are nigger")
        births, _ = await fetch_population_stats()
        await message.answer(f"🍼 Сегодня в Индии родилось: {births}")


    # === 🔘 ОБРАБОТЧИКИ INLINE-КНОПОК ===

    @dp.callback_query(F.data == "nigga_news")
    async def callback_nigga_news(callback: CallbackQuery):
        await callback.message.answer("Niggalink, access the internet and provide me data regarding the criminal activities of black communities in the hoods")
        news = get_news()
        await callback.message.answer(news, parse_mode="HTML")
        await callback.answer("📰 Новости отправлены!")

    @dp.callback_query(F.data == "good_news")
    async def callback_good_news(callback: CallbackQuery):
        await callback.message.answer("You a nigga")
        _, deaths = await fetch_population_stats()
        await callback.message.answer(f"⚰️ Смертей сегодня: {deaths}")
        await callback.answer("✅ Good news sent")

    @dp.callback_query(F.data == "bad_news")
    async def callback_bad_news(callback: CallbackQuery):
        await callback.message.answer("You are nigger")
        births, _ = await fetch_population_stats()
        await callback.message.answer(f"🍼 Рождений сегодня: {births}")
        await callback.answer("⚠️ Bad news received")
