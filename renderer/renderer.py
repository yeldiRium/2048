from abc import ABCMeta
from abc import abstractmethod

from console.output import ConsoleOutput
from gamefield.gamefield import GameField


class Renderer(metaclass=ABCMeta):
    def __init__(self, output_stream: ConsoleOutput):
        self.output_stream = output_stream

    @abstractmethod
    def render(self, game_field: GameField) -> None:
        pass
