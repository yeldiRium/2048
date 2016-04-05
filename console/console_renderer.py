from console.output import ConsoleOutput
from gamefield.gamefield import GameField
from renderer.renderer import Renderer


class ConsoleRenderer(Renderer):
    def __init__(self, output_stream: ConsoleOutput):
        self.output_stream = output_stream

    def render(self, game_field: GameField):
        self.output_stream.write('rendering...')
