import unittest

from gamefield.gamefield import GameField


class BasicGameFieldTestCase(unittest.TestCase):
    def setUp(self):
        # basic_field instantiates a GameField and fills it with TileContainers
        # and empty Tiles
        self.game_field = GameField.basic_field()

    def test_basicFieldWasConstructedCorrectly(self):
        """
        The BasicField should be a GameField of size 4x4 filled with EmptyTiles.
        """
        self.fail()

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
