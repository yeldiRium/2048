from controller.game_controller import GameController
from gamefield.gamefield import GameField
from gamefield.tilecollection import TileCollection
from exceptions import GameLostError, InvalidActionError

tile_collection = TileCollection()
game_field = GameField.basic_field(tile_collection)
game_controller = GameController(game_field, tile_collection)

# If the game was not initialized yet, the score is not accessible
try:
    game_controller.score
except GameNotInitializedError as e:
    print(e)

game_controller.initialize()

# score is returned after each action and each action can raise an
# InvalidActionError if the called action can't be executed:
try:
    score = game_controller.swipe_north_action()
    score = game_controller.swipe_east_action()
    score = game_controller.swipe_south_action()
    score = game_controller.swipe_west_action()
except InvalidActionError as e:
    print(e)
# score can be accessed at any time:
score = game_controller.score

# when there is no move left, a GameLostError is raised:
try:
    game_controller.swipe_east_action()
except GameLostError as e:
    print(e)