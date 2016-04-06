from typing import Iterable

from gamefield.gamefield import GameField
from gamefield.tile import Tile
from gamefield.tilecollection import TileCollection
from gamefield.tilecontainer import TileContainer


class GameController(object):
    def __init__(self, game_field: GameField, tile_collection: TileCollection):
        self.game_field = game_field
        self.tile_collection = tile_collection

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
        # first reset the fused status of each TileContainer:
        for col in self.game_field.field_data:
            for tile_container in col:
                tile_container.fused = False
        # then iterate over the iterator and move/fuse the Tiles.
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

    @staticmethod
    def _moveable(source_tile: Tile, target_tile: Tile) -> bool:
        return source_tile.can_move_to(target_tile) \
               and target_tile.can_be_replaced_with(source_tile)

    @staticmethod
    def _fuseable(source_tile: Tile, target_tile: Tile) -> bool:
        return source_tile.can_fuse_with(target_tile) \
               and target_tile.can_accept_fusion_with(source_tile)
