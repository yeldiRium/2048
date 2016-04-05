from gamefield.gamefield import GameField
from renderer.renderer import Renderer
from renderer.console_renderer import ConsoleRenderer
from game_controller import GameController


class App(object):
    def __init__(self):
        self.game_field = GameField.basic_field()
        self.game_controller = GameController(self.game_field)
        self.renderer = ConsoleRenderer()  # type: Renderer

    def input_invalid(self, user_input: str) -> bool:
        return user_input not in ['n', 'e', 's', 'w', 'q']

    def run(self):
        while True:
            self.renderer.render(self.game_field)
            user_input = input('Wohin swipen? n/e/s/w | q for exit')
            if self.input_invalid(user_input):
                print('Ungültiger Input, bitte wiederholen.')
                continue
            else:
                if user_input == 'n':
                    print("swiping north")
                    self.game_controller.swipeNorthAction()
                elif user_input == 'e':
                    print("swiping east")
                    self.game_controller.swipeEastAction()
                elif user_input == 's':
                    print("swiping south")
                    self.game_controller.swipeSouthAction()
                elif user_input == 'w':
                    print("swiping west")
                    self.game_controller.swipeWestAction()
                else:
                    exit()
