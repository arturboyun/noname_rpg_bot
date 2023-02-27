from typing import Union

from bot.models import Player
from bot.services.base import Service
from bot.types import ID_TYPE


class PlayerService(Service):
    def get(self, pk: ID_TYPE) -> Player | None:
        return await Player.filter(id=pk).first()

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def player_exists(self) -> bool:
        return self.player is not None

    def get_info(self) -> str:
        if self.player is None:
            raise "Player not found."
        return f"Username: {self.player.username}\n" \
               f"Nickname: {self.player.nickname}\n" \
               f"Level: {self.player.lvl}\n" \
               f"XP: {self.player.xp}\n" \
               f"HP: {self.player.hp} / {self.player.max_hp}"
