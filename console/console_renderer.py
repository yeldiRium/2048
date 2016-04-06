from collections import defaultdict

from console.output import ConsoleOutput
from gamefield.gamefield import GameField
from renderer.renderer import Renderer


class ConsoleRenderer(Renderer):
    def render(self, game_field: GameField, score: int):
        print('score: ' + str(score))
        output = defaultdict(str)
        for col in game_field.field_data:
            for i, tile_container in enumerate(col):
                output[i] += '|' + self.left_pad(str(tile_container.tile), 4)

        for _, line in output.items():
            line += '|'

        dashes = ''.join(['-----' for _ in game_field.field_data])
        for _, line in output.items():
            print(dashes)
            print(line)
        print(dashes)

    def left_pad(self, string, size, fill=' '):
        fillers = ''.join([fill for i in range(size)])  # type: str
        l = len(string)
        if l < size:
            return fillers[:(size - l)] + string
        return string
