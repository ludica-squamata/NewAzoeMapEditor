from pygame import image, Surface, K_LEFT, K_RIGHT, K_UP, K_DOWN
from frontend.widgets import BaseWidget
from os import getcwd, path


class MapArea(BaseWidget):
    pos_x = 0
    pos_y = 0

    def __init__(self, parent, **pos):
        super().__init__(parent)
        self.map = image.load(path.join(getcwd(), 'data', 'test_map.png')).convert_alpha()
        self.image = Surface((640, 480))
        self.rect = self.image.get_rect(**pos)
        self.show()

    def on_key_down(self, event):
        if event.key == K_LEFT:
            self.pan('left', -10)
        elif event.key == K_RIGHT:
            self.pan('right', 10)
        if event.key == K_UP:
            self.pan('up', -10)
        if event.key == K_DOWN:
            self.pan('down', 10)

    def on_mousemotion(self, event):
        if self.has_mouse_over and self.is_pressed:
            dx, dy = event.rel
            if dx > 0:
                self.pan('right', dx)
            elif dx < 0:
                self.pan('left', dx)
            if dy < 0:
                self.pan('up', dy)
            elif dy > 0:
                self.pan('down', dy)

    def on_mousebutton_up(self, event):
        if event.button == 1:
            self.is_pressed = False

    def pan(self, key, delta):
        self.dirty = 1
        if key == 'left' and self.pos_x + delta >= -160:
            self.pos_x += delta
        elif key == 'right' and self.pos_x + delta <= 0:
            self.pos_x += delta
        if key == 'up' and self.pos_y + delta >= -321:
            self.pos_y += delta
        if key == 'down' and self.pos_y + delta <= 0:
            self.pos_y += delta

    def update(self):
        self.image.fill((0, 0, 0))
        self.image.blit(self.map, (self.pos_x, self.pos_y))
