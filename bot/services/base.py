from abc import ABC, abstractmethod
from typing import Type

from bot.types import ID_TYPE
from tortoise import Model


class Service(ABC):

    @abstractmethod
    def get(self, pk: ID_TYPE) -> Type[Model] | None:
        pass

    @abstractmethod
    def create(self) -> Type[Model] | None:
        pass

    @abstractmethod
    def update(self) -> Type[Model] | None:
        pass

    @abstractmethod
    def delete(self) -> int:
        pass
