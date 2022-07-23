from .contantes import COLOR_LIGHT, COLOR_SHADOW
from pygame import draw


def biselar(imagen, color_a, color_b):
    w, h = imagen.get_size()
    draw.line(imagen, color_b, (0, h - 2), (w - 2, h - 2), 4)
    draw.line(imagen, color_b, (w - 2, h - 2), (w - 2, 0), 4)
    draw.lines(imagen, color_a, 0, [(w - 4, 0), (0, 0), (0, h - 2)], 4)
    return imagen


def raised_border(imagen):
    return biselar(imagen, COLOR_LIGHT, COLOR_SHADOW)


def sunken_border(imagen):
    return biselar(imagen, COLOR_SHADOW, COLOR_LIGHT)
