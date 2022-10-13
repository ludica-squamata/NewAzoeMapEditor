from ..basewidget import BaseWidget


class BaseButton(BaseWidget):
    img_uns = None
    img_sel = None
    img_dis = None
    img_pre = None

    method = None

    def set_method(self, method):
        self.method = method

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
        if event.button == 1 and self.is_enabled:
            self.is_pressed = True
            self.image = self.img_pre

    def on_mousebutton_up(self, event):
        if event.button == 1 and self.is_enabled:
            self.is_pressed = False
            self.image = self.img_uns
            if self.method is not None:
                self.method()
