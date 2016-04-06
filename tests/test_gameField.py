import unittest

from gamefield.gamefield import GameField
from gamefield.tilecollection import TileCollection
from gamefield.tilecontainer import TileContainer
from gamefield.tile import EmptyTile


class BasicGameFieldTestCase(unittest.TestCase):
    def setUp(self):
        # basic_field instantiates a GameField and fills it with TileContainers
        # and empty Tiles
        self.tile_collection = TileCollection()
        self.game_field = GameField.basic_field(self.tile_collection)

    def test_basicFieldWasConstructedCorrectly(self):
        """
        The BasicField should be a GameField of size 4x4 filled with EmptyTiles.
        Coordinates: 0x is on the left, 0y is at the top
        """
        for x in range(4):
            for y in range(4):
                self.assertIsInstance(
                    self.game_field.field_data[x][y],
                    TileContainer
                )
                self.assertIsInstance(
                    self.game_field.field_data[x][y].tile,
                    EmptyTile
                )

    def test_northIterator(self):
        """
        Tests, that the game_field returs a correctly configured Iterator for
        GameField traversal on swiping north.
        """
        field_iterator = self.game_field.get_north_iterator()
        for i, tile_path in enumerate(field_iterator):
            for j, target_tile in enumerate(tile_path):
                self.assertEqual(target_tile, self.game_field.field_data[i % 4][int(i / 4) - j])
                self.assertIsInstance(target_tile, TileContainer)

    def test_eastIterator(self):
        """
        Tests, that the game_field returs a correctly configured Iterator for
        GameField traversal on swiping east.
        """
        field_iterator = self.game_field.get_east_iterator()
        for i, tile_path in enumerate(field_iterator):
            for j, target_tile in enumerate(tile_path):
                self.assertEqual(target_tile, self.game_field.field_data[3 - int(i / 4) + j][i % 4])
                self.assertIsInstance(target_tile, TileContainer)

    def test_southIterator(self):
        """
        Tests, that the game_field returs a correctly configured Iterator for
        GameField traversal on swiping south.
        """
        field_iterator = self.game_field.get_south_iterator()
        for i, tile_path in enumerate(field_iterator):
            for j, target_tile in enumerate(tile_path):
                self.assertEqual(target_tile, self.game_field.field_data[i % 4][3 - int(i / 4) + j])
                self.assertIsInstance(target_tile, TileContainer)

    def test_westIterator(self):
        """
        Tests, that the game_field returs a correctly configured Iterator for
        GameField traversal on swiping west.
        """
        field_iterator = self.game_field.get_west_iterator()
        for i, tile_path in enumerate(field_iterator):
            for j, target_tile in enumerate(tile_path):
                self.assertEqual(target_tile, self.game_field.field_data[int(i / 4) - j][i % 4])
                self.assertIsInstance(target_tile, TileContainer)
