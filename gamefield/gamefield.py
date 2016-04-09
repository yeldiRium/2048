from typing import Iterable

from gamefield.tilecollection import TileCollection
from gamefield.tilecontainer import TileContainer


class GameField(object):
    """
    The GameField stores all the Tiles inside of TileContainers. It is responsi-
    ble for iterating over the geometrical representation of the field.
    """
    @staticmethod
    def basic_field(tile_collection: TileCollection) -> 'GameField':
        """
        Sets up a GameField with all its default values.
        """
        return GameField(tile_collection)

    def __init__(
            self,
            tile_collection: TileCollection,
            width: int = 4,
            height: int = 4
    ):
        """
        Creates a field of width*height EmptyTiles.
        """
        self._width = width
        self._height = height
        self.field_data = \
            [
                [TileContainer.empty(tile_collection) for _ in range(height)]
                for _ in range(width)
            ]

    def get_north_iterator(self) -> Iterable[Iterable[TileContainer]]:
        """
        Creates an Iterator that iterates over TileContainers for calculation of
        a northward swipe.
        Iteration looks like this: (for 4x4)
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
        return ((self.field_data[i % self._width][int(i / self._width) - j] for j in range(int(i / self._width) + 1)) for i in range(self._width * self._height))

    def get_east_iterator(self) -> Iterable[Iterable[TileContainer]]:
        """
        Creates an Iterator that iterates over TileContainers for calculation of
        an eastward swipe.
        Iteration looks like this: (for 4x4)
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
        return ((self.field_data[self._width - 1 - int(i / self._width) + j][i % self._width] for j in range(int(i / self._width) + 1)) for i in range(self._width * self._height))

    def get_south_iterator(self) -> Iterable[Iterable[TileContainer]]:
        """
        Creates an Iterator that iterates over TileContainers for calculation of
        a southward swipe.
        Iteration looks like this: (for 4x4)
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
        return ((self.field_data[i % self._width][self._width - 1 - int(i / self._width) + j] for j in range(int(i / self._width) + 1)) for i in range(self._width * self._height))

    def get_west_iterator(self) -> Iterable[Iterable[TileContainer]]:
        """
        Creates an Iterator that iterates over TileContainers for calculation of
        an westward swipe.
        Iteration looks like this: (for 4x4)
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
        return ((self.field_data[int(i / self._width) - j][i % self._width] for j in range(int(i / self._width) + 1)) for i in range(self._width * self._height))
