import unittest
from unittest.mock import create_autospec
from controller.game_controller import GameController
from gamefield.gamefield import GameField


class GameControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.game_field = create_autospec(GameField)
        self.game_controller = GameController(self.game_field)

    def test_swipeNorth(self):
        """
        Test that issueing a swipeNorthAction moves the Tiles on the game_field
        correctly to the north.
        """
        self.fail()

    def test_swipeEast(self):
        """
        Test that issueing a swipeNorthAction moves the Tiles on the game_field
        correctly to the east.
        """
        self.fail()

    def test_swipeSouth(self):
        """
        Test that issueing a swipeNorthAction moves the Tiles on the game_field
        correctly to the south.
        """
        self.fail()

    def test_swipeWest(self):
        """
        Test that issueing a swipeNorthAction moves the Tiles on the game_field
        correctly to the west.
        """
        self.fail()
