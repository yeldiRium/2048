import unittest

from gamefield.tile import EmptyTile, BlockingTile, ValueTile
from gamefield.tilecollection import TileCollection


class TileCollectionTestCase(unittest.TestCase):
    def setUp(self):
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
        self.assertEqual(
            self.tile_collection.get_tile('value', value=2),
            self.tile_collection.get_tile('value', value=2)
        )
        self.assertEqual(
            self.tile_collection.get_tile('value', value=4),
            self.tile_collection.get_tile('value', value=4)
        )
        self.assertNotEqual(
            self.tile_collection.get_tile('value', value=2),
            self.tile_collection.get_tile('value', value=4)
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
        self.assertIsInstance(
            self.tile_collection.get_tile('value', value=1),
            ValueTile
        )

    def test_invalidTypeRaisesException(self):
        with self.assertRaises(Exception):
            self.tile_collection.get_tile('invalid_tilename')

    def test_fuse(self):
        """
        Tests that fusing two value tiles returns a ValueTile with their sum as
        its value and the resulting score.
        """
        self.assertEqual(
            (self.tile_collection.get_tile('value',  value=32), 32),
            self.tile_collection.fuse(
                self.tile_collection.get_tile('value',  value=16),
                self.tile_collection.get_tile('value',  value=16)
            )
        )
        # this is technically illegal in the game, but works for engine purpo-
        # ses:
        self.assertEqual(
            (self.tile_collection.get_tile('value',  value=12), 12),
            self.tile_collection.fuse(
                self.tile_collection.get_tile('value',  value=4),
                self.tile_collection.get_tile('value',  value=8)
            )
        )

        with self.assertRaises(Exception):
            self.tile_collection.fuse(
                self.tile_collection.get_tile('empty'),
                self.tile_collection.get_tile('value',  value=8)
            )
