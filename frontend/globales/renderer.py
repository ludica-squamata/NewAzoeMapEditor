from pygame import display, RESIZABLE, SCALED, init as pygame_init
from backend.eventhandler import EventHandler
from pygame.sprite import LayeredUpdates


class Renderer:
    contents = None

    @classmethod
    def init(cls):
        pygame_init()
        display.set_mode((1360, 705), RESIZABLE, SCALED)
        cls.contents = LayeredUpdates()

    @classmethod
    def update(cls):
        fondo = display.get_surface()

        rets = cls.contents.draw(fondo)

        display.update(rets)


EventHandler.register(lambda e: Renderer.init(), 'Init')
