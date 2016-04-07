import unittest

from gamefield.tilecollection import TileCollection


class EmptyTileTestCase(unittest.TestCase):
    def setUp(self):
        self.tile_collection = TileCollection()
        self.test_tile = self.tile_collection.get_tile('empty')
        self.empty_tile = self.test_tile
        self.blocking_tile = self.tile_collection.get_tile('blocking')
        self.value_tile = self.tile_collection.get_tile('value', value=4)

    def test_to_str(self):
        self.assertEqual(' ', str(self.test_tile))

    def test_movingToEmptyTile(self):
        self.assertTrue(self.test_tile.can_be_replaced_with(self.empty_tile))
        self.assertTrue(self.test_tile.can_be_replaced_with(self.blocking_tile))
        self.assertTrue(self.test_tile.can_be_replaced_with(self.value_tile))

    def test_movingEmptyTile(self):
        self.assertFalse(self.test_tile.can_move_to(self.empty_tile))
        self.assertFalse(self.test_tile.can_move_to(self.blocking_tile))
        self.assertFalse(self.test_tile.can_move_to(self.value_tile))

    def test_fusingWithEmptyTile(self):
        self.assertFalse(self.test_tile.can_fuse_with(self.empty_tile))
        self.assertFalse(self.test_tile.can_fuse_with(self.blocking_tile))
        self.assertFalse(self.test_tile.can_fuse_with(self.value_tile))

    def test_fusingEmptyTile(self):
        self.assertFalse(self.test_tile.can_accept_fusion_with(self.empty_tile))
        self.assertFalse(self.test_tile.can_accept_fusion_with(self.blocking_tile))
        self.assertFalse(self.test_tile.can_accept_fusion_with(self.value_tile))


class BlockingTileTestCase(unittest.TestCase):
    def setUp(self):
        self.tile_collection = TileCollection()
        self.test_tile = self.tile_collection.get_tile('blocking')
        self.empty_tile = self.tile_collection.get_tile('empty')
        self.blocking_tile = self.test_tile
        self.value_tile = self.tile_collection.get_tile('value', value=4)

    def test_to_str(self):
        self.assertEqual('x', str(self.test_tile))

    def test_movingToBlockingTile(self):
        self.assertFalse(self.test_tile.can_be_replaced_with(self.empty_tile))
        self.assertFalse(self.test_tile.can_be_replaced_with(self.blocking_tile))
        self.assertFalse(self.test_tile.can_be_replaced_with(self.value_tile))

    def test_movingBlockingTile(self):
        self.assertTrue(self.test_tile.can_move_to(self.empty_tile))
        self.assertFalse(self.test_tile.can_move_to(self.blocking_tile))
        self.assertFalse(self.test_tile.can_move_to(self.value_tile))

    def test_fusingWithBlockingTile(self):
        self.assertFalse(self.test_tile.can_fuse_with(self.empty_tile))
        self.assertFalse(self.test_tile.can_fuse_with(self.blocking_tile))
        self.assertFalse(self.test_tile.can_fuse_with(self.value_tile))

    def test_fusingBlockingTile(self):
        self.assertFalse(self.test_tile.can_accept_fusion_with(self.empty_tile))
        self.assertFalse(self.test_tile.can_accept_fusion_with(self.blocking_tile))
        self.assertFalse(self.test_tile.can_accept_fusion_with(self.value_tile))


class ValueTileTestCase(unittest.TestCase):
    def setUp(self):
        self.tile_collection = TileCollection()
        self.test_tile = self.tile_collection.get_tile('value', value=2)
        self.empty_tile = self.tile_collection.get_tile('empty')
        self.blocking_tile = self.tile_collection.get_tile('blocking')
        self.fitting_value_tile = self.test_tile
        self.unfitting_value_tile = self.tile_collection.get_tile('value', value=4)

    def test_to_str(self):
        self.assertEqual('2', str(self.test_tile))

    def test_movingToValueTile(self):
        self.assertFalse(self.test_tile.can_be_replaced_with(self.empty_tile))
        self.assertFalse(self.test_tile.can_be_replaced_with(self.blocking_tile))
        self.assertFalse(self.test_tile.can_be_replaced_with(self.fitting_value_tile))
        self.assertFalse(self.test_tile.can_be_replaced_with(self.unfitting_value_tile))

    def test_movingValueTile(self):
        self.assertTrue(self.test_tile.can_move_to(self.empty_tile))
        self.assertFalse(self.test_tile.can_move_to(self.blocking_tile))
        self.assertFalse(self.test_tile.can_move_to(self.fitting_value_tile))
        self.assertFalse(self.test_tile.can_move_to(self.unfitting_value_tile))

    def test_fusingWithValueTile(self):
        self.assertFalse(self.test_tile.can_fuse_with(self.empty_tile))
        self.assertFalse(self.test_tile.can_fuse_with(self.blocking_tile))
        self.assertTrue(self.test_tile.can_fuse_with(self.fitting_value_tile))
        self.assertFalse(self.test_tile.can_fuse_with(self.unfitting_value_tile))

    def test_fusingValueTile(self):
        self.assertFalse(self.test_tile.can_accept_fusion_with(self.empty_tile))
        self.assertFalse(self.test_tile.can_accept_fusion_with(self.blocking_tile))
        self.assertTrue(self.test_tile.can_accept_fusion_with(self.fitting_value_tile))
        self.assertFalse(self.test_tile.can_accept_fusion_with(self.unfitting_value_tile))
