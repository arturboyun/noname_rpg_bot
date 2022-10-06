from aiogram import Router, types
from aiogram.filters import Command
from aiogram.handlers import MessageHandler

from bot.services.player import PlayerService

router = Router()


class MyHandler(MessageHandler):
    async def handle(self):
        await self.event.answer("test")


class PlayerInfoCmd(MessageHandler):
    def __init__(self):
        super().__init__(Command("player_info"), MyHandler())
        self.service = PlayerService(self.event.from_user.id)
    async def handle(self):
        info = self.service.get_info()
        await self.event.answer(info)


router.message.register(MyHandler, Command(commands=["start"]))
router.message.register(PlayerInfoCmd, Command(commands=["me", "info"]))
