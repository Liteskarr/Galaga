import math

import pygame
from PIL import Image

if not pygame.get_init():
    pygame.init()


def unpack_tileset(image: Image.Image, xstep: int, ystep: int) -> list:
    """
    Returns tileset from image.
    :param image: PIL image.
    :param xstep: Width of tile.
    :param ystep: Height of tile.
    :return: list[list[pygame.Surface]]
    """
    width, height = image.size
    xsize, ysize = math.ceil(width / xstep), math.ceil(height / ystep)
    result = [[None] * xsize] * ysize
    for x in range(xsize):
        for y in range(ysize):
            crop = image.crop((x * xstep, y * ystep, (x + 1) * xstep, (y + 1) * ystep)).copy()
            size = crop.size
            buffer = crop.tobytes()
            mode = crop.mode
            result[y][x] = pygame.image.fromstring(buffer, size, mode)
    return result
