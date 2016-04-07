from typing import Tuple

from controller.game_controller import GameController
from exceptions import InvalidActionError, GameLostError
from gamefield.gamefield import GameField
from gamefield.tilecollection import TileCollection
import random
import time
from datetime import datetime


def get_current_millis() -> int:
    then = datetime.now()
    return time.mktime(then.timetuple())*1e3 + then.microsecond/1e3


def random_data(
        tile_collection: TileCollection,
        random: random.Random
) -> Tuple[int, int]:
    """
    Simulates a randomly swiping user and returns the score and the number of
    made valid moves.
    :param tile_collection:
    :param random:
    :return:
    """
    game_field = GameField(tile_collection)
    game_controller = GameController(game_field, tile_collection)
    game_controller.initialize()

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
    return game_controller.score, moves


random_gen = random.Random()
tile_collection = TileCollection()
n = 100

print(str(get_current_millis()))
start = get_current_millis()

data = [random_data(tile_collection, random_gen) for i in range(n)]

delta = get_current_millis() - start
print('It takes about ' + str(delta / n) + 'milliseconds per simulation.')

score_sum = 0
move_sum = 0
for score, moves in data:
    score_sum += score
    move_sum += moves
print('On average, a score of ' + str(score_sum / n) + ' is reached and ' +
      str(move_sum / n) + ' moves are executed. (n = ' + str(n) + ')')
