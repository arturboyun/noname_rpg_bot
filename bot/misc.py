import logging
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis

from bot.settings import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("bot.main")

app_dir: Path = Path(__file__).parent.parent
bot = Bot(token=config.bot_token.get_secret_value())
redis = Redis.from_url(config.REDIS_URI)
storage = RedisStorage(redis=redis)
dp = Dispatcher()


async def setup():
    logger.info("Setting up bot misc...")
    from bot.handlers.player.router import router as player_router

    dp.include_router(player_router)


async def start_pooling(skip_updates=True):
    logger.info("Starting bot...")
    await bot.delete_webhook(drop_pending_updates=skip_updates)
    await dp.start_polling(bot)
