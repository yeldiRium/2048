import unittest
from unittest.mock import create_autospec
from controller.game_controller import GameController
from gamefield.gamefield import GameField
from gamefield.tilecollection import TileCollection
from exceptions import GameNotInitializedError


class GameControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.tile_collection = TileCollection()
        self.game_field = create_autospec(GameField)
        self.game_field.field_data = {}
        self.game_controller = GameController(self.game_field, self.tile_collection)
        self.game_controller._random.seed(1337)

    def test_initialize(self):
        """
        Tests that initialization places two random Tiles on the GameField.
        """
        game_field = GameField(self.tile_collection)
        game_controller = GameController(game_field, self.tile_collection)
        game_controller._random.seed(1337)
        game_controller.initialize()
        # The spaces which the random tiles occupy are based on the random gene-
        # rator seed and thus are always equal in tests.
        self.assertEqual(
            game_field.field_data[2][1].tile,
            self.tile_collection.get_tile('value', value=2)
        )
        self.assertEqual(
            game_field.field_data[2][3].tile,
            self.tile_collection.get_tile('value', value=4)
        )


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
        game_field = GameField.basic_field(self.tile_collection)
        game_controller = GameController(game_field, self.tile_collection)
        game_controller._random.seed(1337)

        # set up field:
        game_field.field_data[0][0].tile = self.tile_collection.get_tile('value', value=2)
        game_field.field_data[3][0].tile = self.tile_collection.get_tile('value', value=4)
        game_field.field_data[0][1].tile = self.tile_collection.get_tile('value', value=2)
        game_field.field_data[1][1].tile = self.tile_collection.get_tile('value', value=4)
        game_field.field_data[2][1].tile = self.tile_collection.get_tile('value', value=8)
        game_field.field_data[3][1].tile = self.tile_collection.get_tile('value', value=4)
        game_field.field_data[0][2].tile = self.tile_collection.get_tile('value', value=4)
        game_field.field_data[1][2].tile = self.tile_collection.get_tile('value', value=4)
        game_field.field_data[2][2].tile = self.tile_collection.get_tile('value', value=2)
        game_field.field_data[3][2].tile = self.tile_collection.get_tile('value', value=4)
        game_field.field_data[0][3].tile = self.tile_collection.get_tile('value', value=32)
        game_field.field_data[1][3].tile = self.tile_collection.get_tile('value', value=16)
        game_field.field_data[2][3].tile = self.tile_collection.get_tile('value', value=2)
        game_field.field_data[3][3].tile = self.tile_collection.get_tile('value', value=4)

        game_controller.swipe_north_action()

        self.assertEqual(
            self.tile_collection.get_tile('value', value=4),
            game_field.field_data[0][0]._tile
        )
        self.assertEqual(
            self.tile_collection.get_tile('value', value=8),
            game_field.field_data[1][0]._tile
        )
        self.assertEqual(
            self.tile_collection.get_tile('value', value=8),
            game_field.field_data[2][0]._tile
        )
        self.assertEqual(
            self.tile_collection.get_tile('value', value=8),
            game_field.field_data[3][0]._tile
        )
        self.assertEqual(
            self.tile_collection.get_tile('value', value=4),
            game_field.field_data[0][1]._tile
        )
        self.assertEqual(
            self.tile_collection.get_tile('value', value=16),
            game_field.field_data[1][1]._tile
        )
        self.assertEqual(
            self.tile_collection.get_tile('value', value=4),
            game_field.field_data[2][1]._tile
        )
        self.assertEqual(
            self.tile_collection.get_tile('value', value=8),
            game_field.field_data[3][1]._tile
        )
        self.assertEqual(
            self.tile_collection.get_tile('value', value=32),
            game_field.field_data[0][2]._tile
        )
        # One Tile is randomly inserted after swiping
        self.assertEqual(
            self.tile_collection.get_tile('value', value=4),
            game_field.field_data[2][3].tile
        )

    def test_scorekeeping(self) -> None:
        """
        Tests, that swipes return the resulting score and score is accessible.
        The Score numbers are based on the random seed and thus are equal every
        time the Test is run.
        """
        self.game_field = GameField.basic_field(self.tile_collection)
        self.game_controller = GameController(
            self.game_field,
            self.tile_collection
        )
        self.game_controller._random.seed(1337)
        with self.assertRaises(GameNotInitializedError):
            score = self.game_controller.score
        self.game_controller.initialize()

        self.assertEqual(
            0,
            self.game_controller.swipe_east_action()
        )
        self.assertEqual(
            4,
            self.game_controller.swipe_south_action()
        )
        self.assertEqual(
            12,
            self.game_controller.swipe_south_action()
        )
        self.assertEqual(
            16,
            self.game_controller.swipe_south_action()
        )
        self.assertEqual(
            16,
            self.game_controller.swipe_south_action()
        )
        self.assertEqual(
            20,
            self.game_controller.swipe_south_action()
        )
        self.assertEqual(20, self.game_controller.score)

    def test_initialization_enables_score(self):
        """
        Tests, that calling GameController.initialize() allows to acces GameCon-
        troller.score afterwards. Before, it raises a GameNotInitializedError.
        """
        self.game_field = GameField.basic_field(self.tile_collection)
        self.game_controller = GameController(
            self.game_field,
            self.tile_collection
        )

        with self.assertRaises(GameNotInitializedError):
            score = self.game_controller.score
        self.game_controller.initialize()
        self.assertEqual(0, self.game_controller.score)
