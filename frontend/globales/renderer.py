from pygame import display, RESIZABLE, SCALED, init as pygame_init
from backend.eventhandler import EventHandler
from pygame.sprite import LayeredDirty


class Renderer:
    contents = None

    @classmethod
    def init(cls):
        pygame_init()
        display.set_mode((1360, 705), RESIZABLE, SCALED)
        cls.contents = LayeredDirty()

    @classmethod
    def add_widget(cls, widget, layer=0):
        if widget not in cls.contents:
            cls.contents.add(widget, layer=layer)

    @classmethod
    def del_widget(cls, widget):
        cls.contents.remove(widget)

    @classmethod
    def update(cls):
        fondo = display.get_surface()

        rets = cls.contents.draw(fondo)

        display.update(rets)


EventHandler.register(lambda e: Renderer.init(), 'Init')
