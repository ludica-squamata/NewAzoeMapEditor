from frontend.globales.contantes import COLOR_SELECTED, COLOR_TEXT, COLOR_BOX, COLOR_DISABLED
from frontend.globales import sunken_border, raised_border
from .button_base import BaseButton
from pygame import draw, Surface


class CloseTabButton(BaseButton):
    def __init__(self, parent, **position):
        super().__init__(parent)

        self.img_uns = self.create(COLOR_TEXT, 'raised')
        self.img_sel = self.create(COLOR_SELECTED, 'raised')
        self.img_dis = self.create(COLOR_DISABLED, 'raised')
        self.img_pre = self.create(COLOR_SELECTED, 'sunken')

        self.image = self.img_uns
        self.rect = self.image.get_rect(**position)
        self.show()

    @staticmethod
    def create(color, style):
        base = Surface((17, 17))
        base.fill(COLOR_BOX)
        draw.aaline(base, color, [4, 4], [12, 12])
        draw.aaline(base, color, [12, 4], [4, 12])

        if style == 'raised':
            return raised_border(base)
        elif style == 'sunken':
            return sunken_border(base)
