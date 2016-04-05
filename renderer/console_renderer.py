from gamefield.gamefield import GameField
from renderer.renderer import Renderer


class ConsoleRenderer(Renderer):
    def render(self, game_field: GameField):
        print("rendering...")
