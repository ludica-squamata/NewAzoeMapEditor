from frontend.globales import COLOR_TEXT, COLOR_SELECTED, COLOR_DISABLED, COLOR_BOX
from backend.textrect import render_textrect
from .basewidget import BaseWidget
from pygame import font, mouse


class Tab(BaseWidget):
    linked_document = None
    flagged = False
    is_dragged = False

    def __init__(self, parent, name, document, **position):
        super().__init__(parent)
        f = font.SysFont('Verdana', 12)
        w, h = f.size(name)
        self.name = name
        self.w = w + 3
        self.img_uns = render_textrect(name, f, self.w, h + 2, COLOR_TEXT, COLOR_BOX, justification=1)
        self.img_sel = render_textrect(name, f, self.w, h + 2, COLOR_SELECTED, COLOR_BOX, justification=1)
        self.img_dis = render_textrect(name, f, self.w, h + 2, COLOR_DISABLED, COLOR_BOX, justification=1)
        self.linked_document = document
        self.image = self.img_uns
        self.rect = self.image.get_rect(**position)

    def on_mousebutton_down(self, event):
        if event.button == 1:
            self.parent.select_tab(self)
            self.is_pressed = True
            self.select()

    def on_mousebutton_up(self, event):
        if event.button == 1:
            self.is_pressed = False

    def on_mousemotion(self, event):
        if self.is_pressed:
            self.is_dragged = True

    def displace(self):
        dx, dy = mouse.get_pos()
        dx -= self.rect.w // 2
        return dx

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

    def update(self, *args, **kwargs):
        if self.has_mouse_over and self.is_dragged:
            dx = self.displace()
            self.rect.x = dx
            if not self.is_pressed:  # on_mouseup()
                self.parent.relocate_tabs(self, dx)
                self.is_dragged = False
