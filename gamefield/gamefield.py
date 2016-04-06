from typing import Iterable

from gamefield.tilecollection import TileCollection
from gamefield.tilecontainer import TileContainer


class GameField(object):
    # TODO: Iterators currently only work for the BasicField (4x4).
    @staticmethod
    def basic_field(tile_collection: TileCollection) -> 'GameField':
        return GameField(tile_collection)

    def __init__(
            self,
            tile_collection: TileCollection,
            width: int = 4,
            height: int = 4
    ):
        self.field_data = \
            [
                [TileContainer.empty(tile_collection) for _ in range(height)]
                for _ in range(width)
            ]

    def get_north_iterator(self) -> Iterable[Iterable[TileContainer]]:
        """
        Creates an Iterator that iterates over TileContainers for calculation of
        a northward swipe.
        Iteration looks like this:
         0-> 1-> 2-> 3
               ∨
         4-> 5-> 6-> 7
               ∨
         8-> 9->10->11
               ∨
        12->13->14->15
        Each of the elements is itself an iterator going the elements column up-
        wards.
        """
        return ((self.field_data[i % 4][int(i / 4) - j] for j in range(int(i / 4) + 1)) for i in range(16))

    def get_east_iterator(self) -> Iterable[Iterable[TileContainer]]:
        """
        Creates an Iterator that iterates over TileContainers for calculation of
        an eastward swipe.
        Iteration looks like this:
        12  8  4  0
         ∨  ∨  ∨  ∨
        13  9  5  1
         ∨<-∨<-∨<-∨
        14 10  6  2
         ∨  ∨  ∨  ∨
        15 11  7  3
        Each of the elements is itself an iterator going the elements row right-
        wards.
        """
        return ((self.field_data[3 - int(i / 4) + j][i % 4] for j in range(int(i / 4) + 1)) for i in range(16))

    def get_south_iterator(self) -> Iterable[Iterable[TileContainer]]:
        """
        Creates an Iterator that iterates over TileContainers for calculation of
        a southward swipe.
        Iteration looks like this:
        12->13->14->15
               ∧
         8-> 9->10->11
               ∧
         4-> 5-> 6-> 7
               ∧
         0-> 1-> 2-> 3
        Each of the elements is itself an iterator going the elements column
        downwards.
        """
        return ((self.field_data[i % 4][3 - int(i / 4) + j] for j in range(int(i / 4) + 1)) for i in range(16))

    def get_west_iterator(self) -> Iterable[Iterable[TileContainer]]:
        """
        Creates an Iterator that iterates over TileContainers for calculation of
        an westward swipe.
        Iteration looks like this:
         0  4  8 12
         ∧  ∧  ∧  ∧
         1  5  9 13
         ∧->∧->∧->∧
         2  6 10 14
         ∧  ∧  ∧  ∧
         3  7 11 15
        Each of the elements is itself an iterator going the elements row left-
        wards.
        """
        return ((self.field_data[int(i / 4) - j][i % 4] for j in range(int(i / 4) + 1)) for i in range(16))
