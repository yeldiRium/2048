from gamefield.tile import Tile, EmptyTile, BlockingTile


class TileContainer(object):
    def __init__(self, tile):
        self._tile = tile
        self.fused = False

    @staticmethod
    def empty() -> 'TileContainer':
        return TileContainer(EmptyTile())

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
            return BlockingTile()
        else:
            return self._tile

    @tile.setter
    def tile(self, tile: Tile) -> None:
        self._tile = tile
