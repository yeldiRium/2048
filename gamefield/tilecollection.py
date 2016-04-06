from gamefield.tile import Tile, EmptyTile, BlockingTile


class TileCollection(object):
    # TODO: add ValueTile
    def __init__(self):
        self.tile_storage = {}

    def get_tile(self, tile_name: str, *args, **kwargs) -> Tile:
        """
        If the requested tile was not created yet, a new instance is created and
        stored.
        Then the stored instance is returned.
        """
        identifier = (str(tile_name), str(args), str(kwargs))
        if identifier not in self.tile_storage:
            self.tile_storage[identifier] = \
                TileCollection._new_tile(tile_name, args, kwargs)

        return self.tile_storage[identifier]

    @staticmethod
    def _new_tile(tile_name, *args, **kwargs) -> Tile:
        """
        Creates a new Tile based on the given tile_name.
        """
        if tile_name == 'empty':
            return EmptyTile()
        elif tile_name == 'blocking':
            return BlockingTile()
        else:
            raise Exception('Given tile name \'' + tile_name + '\' is invalid.')