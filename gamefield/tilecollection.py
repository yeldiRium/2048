from typing import Tuple

from gamefield.tile import Tile, EmptyTile, BlockingTile, ValueTile


class TileCollection(object):
    """
    The TileCollection stores and administrates Tile objects, following roughly
    the 'flyweight' pattern.

    Tiles can be requested and are created, if they can't be found in the sto-
    rage. Multiple requests to the same kind of Tile all receive the same in-
    stance of the kind.
    """
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
                TileCollection._new_tile(tile_name, *args, **kwargs)

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
        elif tile_name == 'value':
            return ValueTile(value=kwargs['value'])
        else:
            raise Exception('Given tile name \'' + tile_name + '\' is invalid.')

    def fuse(self, source_tile: ValueTile, target_tile: ValueTile) -> Tuple[ValueTile, int]:
        """
        Fuses two ValueTiles to a ValueTile with the sum of their values.
        Raises exceptions for Tiles that are not ValueTiles.
        Returns the fusion's resulting score.
        """
        if not isinstance(source_tile, ValueTile) \
                or not isinstance(target_tile, ValueTile):
            raise Exception('Only ValueTiles can be fused!')
        new_value = source_tile.value + target_tile.value
        return self.get_tile(
            'value',
            value=new_value
        ), new_value
