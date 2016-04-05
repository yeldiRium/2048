import unittest

from gamefield.gamefield import GameField


class GameFieldTestCase(unittest.TestCase):
    def setUp(self):
        self.game_field = GameField()

    def test_northIterator(self):
        """
        Tests, that the game_field returs a correctly configured Iterator for
        GameField traversal on swiping north.
        """
        self.fail()

    def test_eastIterator(self):
        """
        Tests, that the game_field returs a correctly configured Iterator for
        GameField traversal on swiping east.
        """
        self.fail()

    def test_southIterator(self):
        """
        Tests, that the game_field returs a correctly configured Iterator for
        GameField traversal on swiping south.
        """
        self.fail()

    def test_westIterator(self):
        """
        Tests, that the game_field returs a correctly configured Iterator for
        GameField traversal on swiping west.
        """
        self.fail()
