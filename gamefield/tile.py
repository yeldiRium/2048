from abc import ABCMeta, abstractmethod


class Tile(metaclass=ABCMeta):
    pass


class EmptyTile(Tile):
    pass


class BlockingTile(Tile):
    pass
