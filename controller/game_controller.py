from typing import Iterable
import random

from gamefield.gamefield import GameField
from gamefield.tile import Tile, EmptyTile
from gamefield.tilecollection import TileCollection
from gamefield.tilecontainer import TileContainer


class GameController(object):
    def __init__(self, game_field: GameField, tile_collection: TileCollection):
        self.game_field = game_field
        self.tile_collection = tile_collection
        self._random = random.Random()

    def initialize(self) -> None:
        """
        Initializes the GameField with two random Tiles.
        """
        self._add_random_tile()
        self._add_random_tile()

    def _add_random_tile(self) -> None:
        """
        Adds a random ValueTile with value 2 or 4 to the GameField.
        """
        empty_containers = [
            container
            for col in self.game_field.field_data
            for container in col
            if container.tile == self.tile_collection.get_tile('empty')
            ]
        if len(empty_containers) == 0:
            raise Exception('Field is full, no new Tile can be added.')
        chosen_container = self._random.choice(empty_containers)

        assert(isinstance(chosen_container.tile, EmptyTile))
        chosen_container.tile = self._random.choice(
            [self.tile_collection.get_tile('value', value=2) for i in range(4)] +
            [self.tile_collection.get_tile('value', value=4)]
        )

    def swipe_north_action(self) -> None:
        self._swipe(self.game_field.get_north_iterator())

    def swipe_east_action(self) -> None:
        self._swipe(self.game_field.get_east_iterator())

    def swipe_south_action(self) -> None:
        self._swipe(self.game_field.get_south_iterator())

    def swipe_west_action(self) -> None:
        self._swipe(self.game_field.get_west_iterator())

    def _swipe(self, field_iterator: Iterable[Iterable[TileContainer]]) -> None:
        """
        Traverses a given Iterator and moves/fueses Tiles accordingly.
        """
        # iterate over the iterator and move/fuse the Tiles.
        for tile_path in field_iterator:  # type: Iterable[TileContainer]
            path_list = list(tile_path)
            source_tile = path_list[0]  # type: TileContainer
            for target_tile in path_list[1:]:  # type: TileContainer
                if GameController._moveable(source_tile.tile, target_tile.tile):
                    target_tile.tile = source_tile.tile
                    source_tile.tile = self.tile_collection.get_tile('empty')
                    # when we move a tile, we need to move on with the container
                    # too, to keep it in focus
                    source_tile = target_tile
                else:
                    if GameController._fuseable(source_tile.tile, target_tile.tile):
                        target_tile.tile = self.tile_collection.fuse(
                            source_tile.tile,
                            target_tile.tile
                        )
                        source_tile.tile = self.tile_collection.get_tile('empty')
                        target_tile.fused = True
                    break
        # and finally add a new random tile
        try:
            self._add_random_tile()
        except Exception as e:
            pass  # TODO: real exception handling

        # reset the fused status of each TileContainer:
        for col in self.game_field.field_data:
            for tile_container in col:
                tile_container.fused = False

    @staticmethod
    def _moveable(source_tile: Tile, target_tile: Tile) -> bool:
        return source_tile.can_move_to(target_tile) \
               and target_tile.can_be_replaced_with(source_tile)

    @staticmethod
    def _fuseable(source_tile: Tile, target_tile: Tile) -> bool:
        return source_tile.can_fuse_with(target_tile) \
               and target_tile.can_accept_fusion_with(source_tile)
