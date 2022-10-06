from tortoise import Model, fields

from bot.models.base import BaseModel


class Player(BaseModel):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255, unique=True)
    nicknake = fields.CharField(max_length=255, null=True)
    xp = fields.BigIntField(default=0)
    lvl = fields.IntField(default=1)
    hp = fields.IntField(default=10)
    max_hp = fields.IntField(default=10)

    def __repr__(self):
        return f"<Player {self.id} {self.username}>"
