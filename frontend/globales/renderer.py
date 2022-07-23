from pygame import display, RESIZABLE, SCALED, init as pygame_init
from pygame.sprite import LayeredUpdates


class Renderer:
    contents = None

    @classmethod
    def init(cls):
        pygame_init()
        width = display.Info().current_w
        display.set_mode((width, 705), RESIZABLE, SCALED)
        cls.contents = LayeredUpdates()

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
        fondo.fill('red')

        rets = cls.contents.draw(fondo)

        display.update(rets)
