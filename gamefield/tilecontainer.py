from gamefield.tile import Tile, EmptyTile, BlockingTile
from gamefield.tilecollection import TileCollection


class TileContainer(object):
    def __init__(self, tile: Tile, tile_collection: TileCollection):
        self._tile_collection = tile_collection
        self._tile = tile
        self.fused = False

    @staticmethod
    def empty(tile_collection: TileCollection) -> 'TileContainer':
        return TileContainer(tile_collection.get_tile('empty'), tile_collection)

    def fuse(self) -> None:
        if self.fused:
            raise Exception("TileContainer has already fused!")
        self.fused = True

    def reset_fuse(self) -> None:
        if not self.fused:
            raise Exception("TileContainer has not yet fused!")
        self.fused = False

    @property
    def tile(self) -> Tile:
        if self.fused:
            return self._tile_collection.get_tile('blocking')
        else:
            return self._tile

    @tile.setter
    def tile(self, tile: Tile) -> None:
        self._tile = tile
