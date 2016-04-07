from typing import Iterable
import random
from typing import Tuple

from gamefield.gamefield import GameField
from gamefield.tile import Tile, EmptyTile
from gamefield.tilecollection import TileCollection
from gamefield.tilecontainer import TileContainer
from exceptions import GameNotInitializedError, InvalidActionError, \
    NoEmptyContainerError, GameLostError


class GameController(object):
    """
    The GameController operates on the GameField. The GameController contains
    the main game logic.
    It has an api for user input (swipe_*_action) and for returning output to
    the user (return values, score, is_lost).
    """
    def __init__(self, game_field: GameField, tile_collection: TileCollection):
        self.game_field = game_field
        self.tile_collection = tile_collection
        self._random = random.Random()
        self._score = None

    @property
    def score(self):
        """
        Returns the current score of the ongoing game. If the game was not yet
        initialized, it raises an exception.
        :return:
        """
        if self._score is None:
            raise GameNotInitializedError()
        return self._score

    def initialize(self) -> None:
        """
        Initializes the GameField with two random Tiles.
        """
        self._add_random_tile()
        self._add_random_tile()
        self._score = 0

    def _add_random_tile(self) -> None:
        """
        Adds a random ValueTile with value 2 or 4 to the GameField.
        Each free space has the same chance.
        The value 2 has a chance of 80%, while 4 has 20%.
        """
        empty_containers = [
            container
            for col in self.game_field.field_data
            for container in col
            if container.tile == self.tile_collection.get_tile('empty')
            ]
        if len(empty_containers) == 0:
            raise NoEmptyContainerError()
        chosen_container = self._random.choice(empty_containers)

        assert(isinstance(chosen_container.tile, EmptyTile))
        chosen_container.tile = self._random.choice(
            [self.tile_collection.get_tile('value', value=2) for i in range(4)] +
            [self.tile_collection.get_tile('value', value=4)]
        )

    def swipe_north_action(self) -> int:
        """
        Swipes the GameField northwards.
        :return:
        """
        return self._swipe(self.game_field.get_north_iterator())

    def swipe_east_action(self) -> int:
        """
        Swipes the GameField eastwards.
        :return:
        """
        return self._swipe(self.game_field.get_east_iterator())

    def swipe_south_action(self) -> int:
        """
        Swipes the GameField southwards.
        :return:
        """
        return self._swipe(self.game_field.get_south_iterator())

    def swipe_west_action(self) -> int:
        """
        Swipes the GameField westwards.
        :return:
        """
        return self._swipe(self.game_field.get_west_iterator())

    def _swipe(self, field_iterator: Iterable[Iterable[TileContainer]]) -> int:
        """
        Traverses a given Iterator and moves/fuses Tiles accordingly.
        """
        # first check if the game is lost
        if self.is_lost:
            raise GameLostError()

        # store the current score to add the fuse_score to it, if one is created
        score = self._score or 0
        gamefield_changed = False
        # iterate over the iterator and move/fuse the Tiles.
        for tile_path in field_iterator:  # type: Iterable[TileContainer]
            # transform the iterator to a list to be able to take the first ele-
            # ment out:
            path_list = list(tile_path)
            source_tile = path_list[0]  # type: TileContainer
            for target_tile in path_list[1:]:  # type: TileContainer
                if GameController._moveable(source_tile.tile, target_tile.tile):
                    target_tile.tile = source_tile.tile
                    source_tile.tile = self.tile_collection.get_tile('empty')
                    # when we move a tile, we need to move on with the container
                    # too, to keep it in focus
                    source_tile = target_tile
                    gamefield_changed = True
                else:
                    if GameController._fuseable(source_tile.tile, target_tile.tile):
                        target_tile.tile, fuse_score = self.tile_collection.fuse(
                            source_tile.tile,
                            target_tile.tile
                        )
                        source_tile.tile = self.tile_collection.get_tile('empty')
                        target_tile.fused = True
                        score += fuse_score
                        gamefield_changed = True
                    break
        # if the GameField has not changed during the action, it was an invalid
        # action
        if gamefield_changed is False:
            raise InvalidActionError()

        try:
            # finally add a new random tile
            # raises exception if there is no space left
            self._add_random_tile()
        except NoEmptyContainerError:
            # no new tile can be placed, no problem. If the game is lost, it
            # will be determined with the next swipe.
            pass

        # reset the fused status of each TileContainer:
        for col in self.game_field.field_data:
            for tile_container in col:
                tile_container.fused = False

        if self._score is not None:
            self._score = score

        return self._score or score

    @staticmethod
    def _moveable(source_tile: Tile, target_tile: Tile) -> bool:
        return source_tile.can_move_to(target_tile) \
               and target_tile.can_be_replaced_with(source_tile)

    @staticmethod
    def _fuseable(source_tile: Tile, target_tile: Tile) -> bool:
        return source_tile.can_fuse_with(target_tile) \
               and target_tile.can_accept_fusion_with(source_tile)

    @property
    def is_lost(self) -> int:
        """
        Returns True if there is no possible action left to take.
        Possible TODO: could be slow. if there are performance issues, maybe re-
            view.
        """
        # check for each direction, if an action can be performed
        for field_iterator in [
                self.game_field.get_north_iterator(),
                self.game_field.get_east_iterator(),
                self.game_field.get_south_iterator(),
                self.game_field.get_west_iterator()
        ]:
            # Iterate over the iterator for the current direction and test, if
            # any Tile can be moved or fused.
            for tile_path in field_iterator:  # type: Iterable[TileContainer]
                path_list = list(tile_path)
                source_tile = path_list[0]  # type: TileContainer
                for target_tile in path_list[1:]:  # type: TileContainer
                    if GameController._moveable(
                            source_tile.tile,
                            target_tile.tile
                    ):
                        return False
                    else:
                        if GameController._fuseable(
                                source_tile.tile,
                                target_tile.tile
                        ):
                            return False
                        break
        else:
            return True
