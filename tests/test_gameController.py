import unittest
from unittest.mock import create_autospec
from controller.game_controller import GameController
from gamefield.gamefield import GameField
from gamefield.tilecollection import TileCollection


class GameControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.game_field = create_autospec(GameField)
        self.game_controller = GameController(self.game_field)

    def test_swipeNorth(self):
        """
        Test that issueing a swipeNorthAction uses the north-ward iterator.
        """
        self.game_controller.swipe_north_action()
        self.game_field.get_north_iterator.assert_any_call()

    def test_swipeEast(self):
        """
        Test that issueing a swipeNorthAction uses the east-ward iterator.
        """
        self.game_controller.swipe_east_action()
        self.game_field.get_east_iterator.assert_any_call()

    def test_swipeSouth(self):
        """
        Test that issueing a swipeNorthAction uses the south-ward iterator.
        """
        self.game_controller.swipe_south_action()
        self.game_field.get_south_iterator.assert_any_call()

    def test_swipeWest(self):
        """
        Test that issueing a swipeNorthAction uses the west-ward iterator.
        """
        self.game_controller.swipe_west_action()
        self.game_field.get_west_iterator.assert_any_call()

    def test_swipe(self):
        """
        Functional test that a swipe action correctly traverses the created
        iterator.
        The field is layed out like this:
         2  x  x  4
         2  4  8  4
         4  4  2  4
        32 16  2  4
        The result should be this: (northward swipe)
         4  8  8  8
         4 16  4  8
        32  x  x  x
         x  x  x  x
        """
        tile_collection = TileCollection()
        game_field = GameField.basic_field(tile_collection)

        # set up field:
        game_field.field_data[0][0] = tile_collection.get_tile('value', 2)
        game_field.field_data[3][0] = tile_collection.get_tile('value', 4)
        game_field.field_data[0][1] = tile_collection.get_tile('value', 2)
        game_field.field_data[1][1] = tile_collection.get_tile('value', 4)
        game_field.field_data[2][1] = tile_collection.get_tile('value', 8)
        game_field.field_data[3][1] = tile_collection.get_tile('value', 4)
        game_field.field_data[0][2] = tile_collection.get_tile('value', 4)
        game_field.field_data[1][2] = tile_collection.get_tile('value', 4)
        game_field.field_data[2][2] = tile_collection.get_tile('value', 2)
        game_field.field_data[3][2] = tile_collection.get_tile('value', 4)
        game_field.field_data[0][3] = tile_collection.get_tile('value', 32)
        game_field.field_data[1][3] = tile_collection.get_tile('value', 16)
        game_field.field_data[2][3] = tile_collection.get_tile('value', 2)
        game_field.field_data[3][3] = tile_collection.get_tile('value', 4)

        self.game_controller.swipe_north_action()

        self.assertEqual(
            tile_collection.get_tile('value', 4),
            game_field.field_data[0][0]
        )
        self.assertEqual(
            tile_collection.get_tile('value', 8),
            game_field.field_data[1][0]
        )
        self.assertEqual(
            tile_collection.get_tile('value', 8),
            game_field.field_data[2][0]
        )
        self.assertEqual(
            tile_collection.get_tile('value', 8),
            game_field.field_data[3][0]
        )
        self.assertEqual(
            tile_collection.get_tile('value', 4),
            game_field.field_data[0][1]
        )
        self.assertEqual(
            tile_collection.get_tile('value', 16),
            game_field.field_data[1][1]
        )
        self.assertEqual(
            tile_collection.get_tile('value', 4),
            game_field.field_data[2][1]
        )
        self.assertEqual(
            tile_collection.get_tile('value', 8),
            game_field.field_data[3][1]
        )
        self.assertEqual(
            tile_collection.get_tile('value', 32),
            game_field.field_data[1][2]
        )
