from tortoise import Tortoise
from bot.settings import config

TORTOISE_ORM_CONFIG = {
    "connections": {"default": config.POSTGRES_URI},
    "apps": {
        "models": {
            "models": ["aerich.models", "bot.models"],
            "default_connection": "default",
        },
    },
}

async def init():
    await Tortoise.init(TORTOISE_ORM_CONFIG)
    await Tortoise.generate_schemas()
