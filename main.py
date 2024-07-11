import asyncio, logging, sys
from aiogram import Bot, Dispatcher
from handlers import personal_chat, xyapi_chat
from config import TG_TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TG_TOKEN)
dp = Dispatcher()


async def main() -> None:
    dp.include_routers(personal_chat.router, xyapi_chat.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())