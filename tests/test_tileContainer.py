import unittest

from gamefield.tile import EmptyTile
from gamefield.tile import BlockingTile
from gamefield.tilecontainer import TileContainer


class TileContainerTestCase(unittest.TestCase):
    def setUp(self):
        self.empty_tile_container = TileContainer(EmptyTile())
        self.blocking_tile_container = TileContainer(BlockingTile())
        # TODO: add other tiles to containers

    def test_tileProperty(self):
        """
        Asserts that the TileContainer returns its Tile unless it was fused this
        turn, then it returns a BlockingTile.
        """
        self.assertIsInstance(self.empty_tile_container.tile, EmptyTile)
        self.assertIsInstance(self.blocking_tile_container.tile, BlockingTile)
        self.empty_tile_container.fused = True
        self.blocking_tile_container.fused = True
        self.assertIsInstance(self.empty_tile_container.tile, BlockingTile)
        self.assertIsInstance(self.blocking_tile_container.tile, BlockingTile)
