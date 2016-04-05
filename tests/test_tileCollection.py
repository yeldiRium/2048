import unittest

from gamefield.tile import EmptyTile, BlockingTile
from gamefield.tilecollection import TileCollection


class TileCollectionTestCase(unittest.TestCase):
    def setUp(self):
        # TODO: add ValueTile
        self.tile_collection = TileCollection()

    def test_lazyLoading(self):
        """
        The Tiles are only created in storage if the are asked for, not in ad-
        vance.
        """
        with self.assertRaises(Exception):
            _ = self.tile_collection.tile_storage[('blocking', str(()), str({}))]
        tile = self.tile_collection.get_tile('blocking')
        self.assertEqual(tile, self.tile_collection.tile_storage[('blocking', str(()), str({}))])

    def test_identicalInstances(self):
        """
        The Tiles are kept in storage and every time a Tile is asked for, the
        same instance is returned.
        """
        self.assertEqual(
            self.tile_collection.get_tile('empty'),
            self.tile_collection.get_tile('empty')
        )
        self.assertEqual(
            self.tile_collection.get_tile('blocking'),
            self.tile_collection.get_tile('blocking')
        )

    def test_tileTypes(self):
        """
        The different Requests return different Types of Tiles.
        """
        self.assertIsInstance(
            self.tile_collection.get_tile('empty'),
            EmptyTile
        )
        self.assertIsInstance(
            self.tile_collection.get_tile('blocking'),
            BlockingTile
        )

    def test_invalidTypeRaisesException(self):
        with self.assertRaises(Exception):
            self.tile_collection.get_tile('invalid_tilename')