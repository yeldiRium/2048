from abc import ABCMeta
from abc import abstractmethod

from console.output import ConsoleOutput
from gamefield.gamefield import GameField


class Renderer(metaclass=ABCMeta):
    @abstractmethod
    def render(self, game_field: GameField, output_stream: ConsoleOutput) -> None:
        pass
