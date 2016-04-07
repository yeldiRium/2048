from controller.game_controller import GameController
from exceptions import InvalidActionError, GameLostError
from gamefield.gamefield import GameField
from gamefield.tilecollection import TileCollection
import random

"""
This script simulates a player who randomly swipes the game until they lose.
Afterwards, the number of valid swipes and the reached score are displayed.
"""

tile_collection = TileCollection()
game_field = GameField(tile_collection)
game_controller = GameController(game_field, tile_collection)
game_controller.initialize()
random = random.Random()

moves = 0
actions = [
    game_controller.swipe_north_action,
    game_controller.swipe_east_action,
    game_controller.swipe_south_action,
    game_controller.swipe_west_action
]
while True:
    try:
        # do anything
        action = random.choice(actions)
        action()
        moves += 1
    except InvalidActionError as _:
        # if the action was invalid, ignore and keep going
        pass
    except GameLostError as e:
        # if the game is lost, break out of the loop
        if isinstance(e, GameLostError):
            break
# print score
print('Move Counter: ' + str(moves))
print('Score: ' + str(game_controller.score))
