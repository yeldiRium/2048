import unittest

from gamefield.tile import EmptyTile, BlockingTile


class EmptyTileTestCase(unittest.TestCase):
    def setUp(self):
        # TODO: add ValueTile
        self.test_tile = EmptyTile()
        self.empty_tile = self.test_tile
        self.blocking_tile = BlockingTile()

    def test_movingToEmptyTile(self):
        self.assertTrue(self.test_tile.can_be_replaced_with(self.empty_tile))
        self.assertTrue(self.test_tile.can_be_replaced_with(self.blocking_tile))

    def test_movingEmptyTile(self):
        self.assertFalse(self.test_tile.can_move_to(self.empty_tile))
        self.assertFalse(self.test_tile.can_move_to(self.blocking_tile))

    def test_fusingWithEmptyTile(self):
        self.assertFalse(self.test_tile.can_fuse_with(self.empty_tile))
        self.assertFalse(self.test_tile.can_fuse_with(self.blocking_tile))

    def test_fusingEmptyTile(self):
        self.assertFalse(self.test_tile.can_accept_fusion_with(self.empty_tile))
        self.assertFalse(self.test_tile.can_accept_fusion_with(self.blocking_tile))


class BlockingTileTestCase(unittest.TestCase):
    def setUp(self):
        # TODO : add ValueTile
        self.test_tile = BlockingTile()
        self.empty_tile = EmptyTile()
        self.blocking_tile = self.test_tile

    def test_movingToBlockingTile(self):
        self.assertFalse(self.test_tile.can_be_replaced_with(self.empty_tile))
        self.assertFalse(self.test_tile.can_be_replaced_with(self.blocking_tile))

    def test_movingblockingTile(self):
        self.assertTrue(self.test_tile.can_move_to(self.empty_tile))
        self.assertFalse(self.test_tile.can_move_to(self.blocking_tile))

    def test_fusingWithBlockingTile(self):
        self.assertFalse(self.test_tile.can_fuse_with(self.empty_tile))
        self.assertFalse(self.test_tile.can_fuse_with(self.blocking_tile))

    def test_fusingBlockingTile(self):
        self.assertFalse(self.test_tile.can_accept_fusion_with(self.empty_tile))
        self.assertFalse(self.test_tile.can_accept_fusion_with(self.blocking_tile))
