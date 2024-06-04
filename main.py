import asyncio
import logging
from aiogram.client.default import DefaultBotProperties
from aiogram import Dispatcher, Bot, Router
from aiogram.enums import ParseMode
from Configurations.config1 import config_loader
from handlers import user_handlers, other_handlers
from keyboards.main_menu import set_main_menu

logger = logging.getLogger(__name__)


async def main() -> None:
    logging.basicConfig(level=logging.INFO,format='%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s')
    logger.info('Starting')

    config = config_loader('.env')

    bot = Bot(token=config.tg_bot.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    await set_main_menu(bot)
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())
