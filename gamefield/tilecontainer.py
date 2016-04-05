from gamefield.tile import EmptyTile


class TileContainer(object):
    def __init__(self, tile):
        self.tile = tile

    @staticmethod
    def empty() -> 'TileContainer':
        return TileContainer(EmptyTile())
