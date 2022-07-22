from pygame import display, Surface
from frontend.widgets import BaseWidget
from backend.eventhandler import EventHandler
from .map_area import MapArea


class Window(BaseWidget):
    is_selectable = False

    def __init__(self):
        super().__init__()
        self.image = Surface(display.get_window_size())
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.show()

        self.map = MapArea(self, bottom=self.rect.bottom-50, left=self.rect.left+50)


EventHandler.register(lambda e: Window(), 'Init')
