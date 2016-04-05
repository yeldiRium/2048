from abc import ABCMeta, abstractmethod


class Tile(metaclass=ABCMeta):
    @abstractmethod
    def can_move_to(self, tile: 'Tile') -> bool:
        """
        True, if self can move onto the given tile.
        Often calls the given tile for can_be_replaced_with.
        """
        pass

    @abstractmethod
    def can_be_replaced_with(self, tile: 'Tile') -> bool:
        """
        True, if the given tile can be moved onto self.
        """
        pass


class EmptyTile(Tile):
    def can_move_to(self, tile: 'Tile') -> bool:
        return False

    def can_be_replaced_with(self, tile: 'Tile') -> bool:
        return True


class BlockingTile(Tile):
    def can_move_to(self, tile: 'Tile') -> bool:
        return tile.can_be_replaced_with(self)

    def can_be_replaced_with(self, tile: 'Tile') -> bool:
        return False
