from frontend.globales import COLOR_TEXT, COLOR_SELECTED, COLOR_DISABLED, COLOR_BOX
from backend.textrect import render_textrect
from .basewidget import BaseWidget
from pygame import font


class Tab(BaseWidget):
    def __init__(self, parent, text, **position):
        super().__init__(parent)
        f = font.SysFont('Verdana', 12)
        w, h = f.size(text)
        self.img_uns = render_textrect(text, f, w + 2, h + 2, COLOR_TEXT, COLOR_BOX)
        self.img_sel = render_textrect(text, f, w + 2, h + 2, COLOR_SELECTED, COLOR_BOX)
        self.img_dis = render_textrect(text, f, w + 2, h + 2, COLOR_DISABLED, COLOR_BOX)
        self.image = self.img_uns
        self.rect = self.image.get_rect(**position)
