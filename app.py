from console.console_renderer import ConsoleRenderer
from console.input import ConsoleInput
from console.output import ConsoleOutput
from controller.game_controller import GameController
from gamefield.gamefield import GameField
from renderer.renderer import Renderer


class App(object):
    def __init__(
            self,
            input_stream: ConsoleInput,
            output_stream: ConsoleOutput
    ):
        self.input = input_stream
        self.output = output_stream
        self.game_field = GameField.basic_field()
        self.game_controller = GameController(self.game_field)
        self.renderer = ConsoleRenderer(output_stream)  # type: Renderer
        self.prompt_counter = 0

    def input_invalid(self, user_input: str) -> bool:
        return user_input not in ['n', 'e', 's', 'w', 'q']

    def run(self, max_prompts: int = -1):
        run_indefinitely = max_prompts == -1
        runlimit_not_reached_yet = max_prompts > self.prompt_counter

        # render once before everything starts, so the initial field can be seen
        self.renderer.render(self.game_field)

        while run_indefinitely or runlimit_not_reached_yet:
            runlimit_not_reached_yet = max_prompts > self.prompt_counter
            self.prompt_counter += 1
            user_input = self.input.getline('Wohin swipen? n/e/s/w | q for exit')
            if self.input_invalid(user_input):
                self.output.write('Ungültiger Input, bitte wiederholen.')
                continue
            else:
                if user_input == 'n':
                    self.output.write("swiping north")
                    #self.game_controller.swipeNorthAction()
                elif user_input == 'e':
                    self.output.write("swiping east")
                    #self.game_controller.swipeEastAction()
                elif user_input == 's':
                    self.output.write("swiping south")
                    #self.game_controller.swipeSouthAction()
                elif user_input == 'w':
                    self.output.write("swiping west")
                    #self.game_controller.swipeWestAction()
                else:
                    exit()
            # render again after input and calculation
            self.renderer.render(self.game_field)
