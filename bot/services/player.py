from typing import Union
from bot.models import Player

ID_TYPE = Union[int, str]


class PlayerService:
    def __init__(self, player: Union[Player, ID_TYPE]):
        if isinstance(player, Player):
            self.player = player
        else:
            self.player = Player.filter(id=player).first()

    def get_player(self) -> Player:
        return self.player
    def player_exists(self) -> bool:
        return self.player is not None
    def get_info(self) -> str:
        if self.player is None:
            raise "Player not found."
        return f"Username: {self.player.username}\n"\
            f"Nickname: {self.player.nickname}\n"\
            f"Level: {self.player.lvl}\n"\
            f"XP: {self.player.xp}\n"\
            f"HP: {self.player.hp} / {self.player.max_hp}"
