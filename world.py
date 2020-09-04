import pygame

import tile
import unit

if not pygame.get_init():
    pygame.init()


class World:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.tiles: list = [[None] * width] * height

    def test_pos(self, x: int, y: int) -> None:
        if 0 <= x < self.height and 0 <= y < self.width:
            raise IndexError

    def get_tile(self, x: int, y: int) -> tile.Tile:
        """
        Returns tile on {x;y}.
        :param x: X.
        :param y: Y.
        :return: Tile.
        """
        self.test_pos(x, y)
        return self.tiles[x][y]

    def get_unit(self, x: int, y: int) -> unit.Unit:
        """
        Returns unit on {x;y}.
        :param x: X.
        :param y: Y.
        :return: Unit.
        """
        self.test_pos(x, y)
        return self.tiles[x][y]

    def can_unit_move(self, x1: int, y1: int, x2: int, y2: int) -> bool:
        """
        Tests only terrain type.
        :param x1: From X.
        :param y1: From Y.
        :param x2: To X.
        :param y2: To Y.
        :return: Can unit move.
        """
        self.test_pos(x1, y1)
        self.test_pos(x2, y2)
        if self.tiles[x1][x2].unit is None:
            return True
        return self[x1][y1].unit.can_unit_move_on(self.tiles[x2][y2].terrain)

    def move_unit(self, x1: int, y1: int, x2: int, y2: int) -> None:
        """
        Moves unit without game logic.
        :param x1: From X.
        :param y1: From Y.
        :param x2: To X.
        :param y2: To Y.
        """
        self.test_pos(x1, y1)
        self.test_pos(x2, y2)
        self.tiles[x2][y2].unit = self.tiles[x1][y1]

