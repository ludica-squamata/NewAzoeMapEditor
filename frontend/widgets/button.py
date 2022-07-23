from frontend.globales import COLOR_SELECTED, COLOR_TEXT, COLOR_BOX, COLOR_DISABLED, COLOR_LIGHT, COLOR_SHADOW
from frontend.globales import sunken_border, raised_border
from backend.textrect import render_textrect
from .basewidget import BaseWidget
from pygame import font


class Button(BaseWidget):
    def __init__(self, parent, text, method, w, txt_h=16, **postion):
        super().__init__(parent)
        self.img_uns = self.create(text, w, txt_h, COLOR_TEXT, style='raised')
        self.img_sel = self.create(text, w, txt_h, COLOR_SELECTED, style='raised')
        self.img_dis = self.create(text, w, txt_h, COLOR_DISABLED, style='raised')
        self.img_pre = self.create(text, w, txt_h, COLOR_SELECTED, style='sunken')
        self.image = self.img_uns
        self.rect = self.image.get_rect(**postion)
        self.method = method

    @staticmethod
    def create(text, w, txt_h, color, style='raised'):
        f = font.SysFont('Verdana', txt_h)
        base = render_textrect(text, f, w+2, txt_h+2, color, COLOR_BOX)
        if style == 'raised':
            return raised_border(base, COLOR_LIGHT, COLOR_SHADOW)
        elif style == 'sunken':
            return sunken_border(base, COLOR_LIGHT, COLOR_SHADOW)

    def select(self):
        super().select()
        self.image = self.img_sel

    def deselect(self):
        super().deselect()
        self.image = self.img_uns

    def enable(self):
        super().enable()
        self.image = self.img_uns

    def disable(self):
        super().disable()
        self.image = self.img_dis

    def on_mousebutton_down(self, event):
        if event.button == 1:
            self.is_pressed = True
            self.image = self.img_pre

    def on_mousebutton_up(self, event):
        if event.button == 1:
            self.is_pressed = False
            self.image = self.img_uns
            self.method()
