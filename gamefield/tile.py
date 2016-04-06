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

    @abstractmethod
    def can_fuse_with(self, tile: 'Tile') -> bool:
        """
        True, if self can fuse with the given tile.
        """
        pass

    @abstractmethod
    def can_accept_fusion_with(self, tile: 'Tile') -> bool:
        """
        True, if a given tile can fuse with self and take its place.
        """
        pass


class EmptyTile(Tile):
    def can_move_to(self, tile: 'Tile') -> bool:
        """
        Since EmptryTiles don't represent anything other than nothing, it is
        wasted time to move them. So they don't let themselves get moved.
        """
        return False

    def can_be_replaced_with(self, tile: 'Tile') -> bool:
        """
        Since EmptyTiles are supposed to be empty, everything can move onto
        them.
        """
        return True

    def can_fuse_with(self, tile: 'Tile') -> bool:
        """
        EmptyTiles can't fuse with anything.
        """
        return False

    def can_accept_fusion_with(self, tile: 'Tile') -> bool:
        """
        Nothing can be fused onto an EmptyTile.
        """
        return False


class BlockingTile(Tile):
    def can_move_to(self, tile: 'Tile') -> bool:
        """
        BlockingTiles are simple tiles that underlie the usual physical rules
        and can thus be moved onto everything that want to be moved on.
        """
        return tile.can_be_replaced_with(self)

    def can_be_replaced_with(self, tile: 'Tile') -> bool:
        """
        BlockingTiles are simple tiles that take up space and thus other tiles
        can't be moved onto them.
        """
        return False

    def can_fuse_with(self, tile: 'Tile') -> bool:
        """
        BlockingTiles can't fuse with anything.
        """
        return False

    def can_accept_fusion_with(self, tile: 'Tile') -> bool:
        """
        Nothing can be fused onto a BlockingTile.
        """
        return False
