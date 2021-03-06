from console.console_renderer import ConsoleRenderer
from console.input import ConsoleInput
from console.output import ConsoleOutput
from controller.game_controller import GameController
from exceptions import InvalidActionError, GameLostError
from gamefield.gamefield import GameField
from gamefield.tilecollection import TileCollection
from renderer.renderer import Renderer


class App(object):
    """
    The App administrates the game. It instantiates a GameField and a GameCon-
    troller and makes them interact with the user.
    """
    def __init__(
            self,
            input_stream: ConsoleInput,
            output_stream: ConsoleOutput
    ):
        self.input = input_stream
        self.output = output_stream
        self.tile_collection = TileCollection()
        self.game_field = GameField.basic_field(self.tile_collection)
        self.game_controller = GameController(
            self.game_field,
            self.tile_collection
        )
        self.game_controller.initialize()
        self.renderer = ConsoleRenderer(output_stream)  # type: Renderer
        self.prompt_counter = 0

    @staticmethod
    def input_invalid(user_input: str) -> bool:
        """
        Checks if a given user input is valid. Allowed inputs are one charachter
        directions or 'q' to end the application.
        :param user_input:
        """
        return user_input not in ['n', 'e', 's', 'w', 'q']

    def run(self, max_prompts: int = -1):
        """
        Runs the mainloop for a maximum of max_prompts times.
        :param max_prompts:
        """
        run_indefinitely = max_prompts == -1
        run_limit_not_reached_yet = max_prompts > self.prompt_counter

        # render once before everything starts, so the initial field can be seen
        self.renderer.render(self.game_field, self.game_controller.score)

        while run_indefinitely or run_limit_not_reached_yet:
            user_input = self.input.getline(
                'Wohin swipen? n/e/s/w | q for exit\n'
            )
            if self.input_invalid(user_input):
                self.output.write('Ungültiger Input, bitte wiederholen.')
                continue
            else:
                try:
                    if user_input == 'n':
                        self.output.write("swiping north")
                        self.game_controller.swipe_north_action()
                    elif user_input == 'e':
                        self.output.write("swiping east")
                        self.game_controller.swipe_east_action()
                    elif user_input == 's':
                        self.output.write("swiping south")
                        self.game_controller.swipe_south_action()
                    elif user_input == 'w':
                        self.output.write("swiping west")
                        self.game_controller.swipe_west_action()
                    else:
                        exit()
                except (GameLostError, InvalidActionError) as e:
                    if isinstance(e, GameLostError):
                        print("sorry, you lost the game!")
                        exit()
                    else:
                        print("that move was invalid. try again!")
            # render again after input and calculation
            self.renderer.render(self.game_field, self.game_controller.score)

            self.prompt_counter += 1
            run_limit_not_reached_yet = max_prompts > self.prompt_counter
