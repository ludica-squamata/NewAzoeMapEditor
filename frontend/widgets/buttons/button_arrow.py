from frontend.globales.contantes import COLOR_SELECTED, COLOR_TEXT, COLOR_BOX, COLOR_DISABLED
from frontend.globales import sunken_border, raised_border
from .button_base import BaseButton
from pygame import draw, Surface


class ArrowButton(BaseButton):
    def __init__(self, parent, direction, **position):
        super().__init__(parent)

        self.img_uns = self.create(direction, COLOR_TEXT, 'raised')
        self.img_sel = self.create(direction, COLOR_SELECTED, 'raised')
        self.img_dis = self.create(direction, COLOR_DISABLED, 'raised')
        self.img_pre = self.create(direction, COLOR_SELECTED, 'sunken')

        self.image = self.img_uns
        self.rect = self.image.get_rect(**position)
        self.show()

    @staticmethod
    def create(direction, color, style):
        base = Surface((17, 17))
        base.fill(COLOR_BOX)
        points = []
        if direction == 'left':
            points = [[12, 4], [4, 8], [12, 12]]
        elif direction == 'right':
            points = [[4, 4], [12, 8], [4, 12]]
        elif direction == 'up':
            points = [[4, 12], [8, 4], [12, 12]]
        elif direction == 'down':
            points = [[4, 4], [8, 12], [12, 4]]

        draw.aalines(base, color, False, points)

        if style == 'raised':
            return raised_border(base)
        elif style == 'sunken':
            return sunken_border(base)
