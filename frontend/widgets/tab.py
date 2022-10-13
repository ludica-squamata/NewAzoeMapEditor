from frontend.globales import COLOR_TEXT, COLOR_SELECTED, COLOR_DISABLED, COLOR_BOX
from backend.textrect import render_textrect
from .basewidget import BaseWidget
from pygame import font


class Tab(BaseWidget):
    linked_document = None
    flagged = False

    def __init__(self, parent, name, document, **position):
        super().__init__(parent)
        f = font.SysFont('Verdana', 12)
        w, h = f.size(name)
        self.name = name
        self.w = w + 10
        self.img_uns = render_textrect(name, f, self.w, h + 2, COLOR_TEXT, COLOR_BOX, justification=1)
        self.img_sel = render_textrect(name, f, self.w, h + 2, COLOR_SELECTED, COLOR_BOX, justification=1)
        self.img_dis = render_textrect(name, f, self.w, h + 2, COLOR_DISABLED, COLOR_BOX, justification=1)
        self.linked_document = document
        self.image = self.img_uns
        self.rect = self.image.get_rect(**position)

    def on_mousebutton_down(self, event):
        if event.button == 1:
            self.parent.select_tab(self)
            self.select()

    def move(self, direction):
        self.rect.x += (self.w + 1) * direction

    def select(self):
        super().select()
        self.image = self.img_sel

    def deselect(self):
        super().deselect()
        self.image = self.img_uns

    def __repr__(self):
        return f'Tab-{self.name}'
