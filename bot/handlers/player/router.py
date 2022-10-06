from aiogram import Router
from bot.handlers.player.start import router as start_router

router = Router(name="player_router")
router.include_router(start_router)
