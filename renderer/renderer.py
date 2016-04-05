from abc import ABCMeta
from abc import abstractmethod

from gamefield.gamefield import GameField


class Renderer(metaclass=ABCMeta):
    @abstractmethod
    def render(self, game_field: GameField) -> None:
        pass
