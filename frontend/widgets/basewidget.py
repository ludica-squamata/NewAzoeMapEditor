from frontend.globales import Renderer, WidgetHandler
from pygame.sprite import DirtySprite


class BaseWidget(DirtySprite):
    requested_layer = 0
    is_visible = True
    is_selected = False
    is_enabled = True

    is_selectable = True
    has_mouse_over = False
    is_pressed = False

    def __init__(self, parent=None):
        super().__init__()

        if parent is not None:
            self.requested_layer = parent.requested_layer + 1

        self.parent = parent

    def show(self):
        self.is_visible = True
        Renderer.add_widget(self, layer=self.requested_layer)
        WidgetHandler.add_widget(self)

    def hide(self):
        self.is_visible = False
        Renderer.del_widget(self)
        WidgetHandler.del_widget(self)

    def select(self):
        self.is_selected = True
        self.dirty = 1  # because the image will surely change.

    def deselect(self):
        self.is_selected = False
        self.dirty = 1  # same as select()

    def enable(self):
        self.is_enabled = True
        self.dirty = 1  # same as select()

    def disable(self):
        self.is_enabled = False
        self.dirty = 1  # same as select()

    def on_deletion(self, event):
        pass

    def on_focus_in(self, event):
        pass

    def on_focus_out(self, event):
        pass

    def on_key_down(self, event):
        pass

    def on_key_up(self, event):
        pass

    def on_mousebutton_down(self, event):
        pass

    def on_mousebutton_up(self, event):
        pass

    def on_mousemotion(self, event):
        pass

    def on_mouseover(self):
        self.has_mouse_over = True

    def on_video_resize(self):
        self.dirty = 1

    def on_maximize(self):
        self.dirty = 1

    def on_minimize(self):
        self.dirty = 1

    def on_restore(self):
        self.dirty = 1

    def update(self, *args, **kwargs):
        pass
