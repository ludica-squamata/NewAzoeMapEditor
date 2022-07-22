from pygame import K_ESCAPE, VIDEORESIZE, WINDOWRESTORED, WINDOWMAXIMIZED, WINDOWMINIMIZED
from pygame import MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION, KEYDOWN, KEYUP, QUIT
from backend.eventhandler import EventHandler
from backend.groups import WidgetGroup
from pygame import event, mouse
from backend.util import salir


class WidgetHandler:
    widgets = None
    observed_events = None

    @classmethod
    def init(cls):
        cls.widgets = WidgetGroup()
        cls.observed_events = [VIDEORESIZE, WINDOWRESTORED, WINDOWMAXIMIZED, WINDOWMINIMIZED, KEYDOWN, QUIT,
                               MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION]
        event.set_allowed(cls.observed_events)

    @classmethod
    def add_widget(cls, widget, layer=0):
        if widget not in cls.widgets:
            cls.widgets.add(widget, layer=layer)

    @classmethod
    def del_widget(cls, widget):
        widget.on_deletion()
        cls.widgets.remove(widget)

    @classmethod
    def update(cls):
        events = event.get(cls.observed_events)
        event.clear()
        for e in events:
            if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                salir()

            elif e.type == KEYDOWN:
                pass

            elif e.type == KEYUP:
                pass

            elif e.type == MOUSEBUTTONDOWN:
                pass

            elif e.type == MOUSEBUTTONUP:
                pass

            elif e.type == MOUSEMOTION:
                pass

            elif e.type == VIDEORESIZE:
                pass

            elif e.type == WINDOWRESTORED:
                pass

            elif e.type == WINDOWMAXIMIZED:
                pass

            elif e.type == WINDOWMINIMIZED:
                pass

        pos = mouse.get_pos()
        for widget in cls.widgets:
            if widget.rect.collidepoint(pos):
                widget.on_mouseover()

        cls.widgets.update()


EventHandler.register(lambda e: WidgetHandler.init(), 'Init')
