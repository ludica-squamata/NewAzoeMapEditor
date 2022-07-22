from pygame import K_ESCAPE, VIDEORESIZE, WINDOWRESTORED, WINDOWMAXIMIZED, WINDOWMINIMIZED
from pygame import MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION, KEYDOWN, KEYUP, QUIT
from backend.eventhandler import EventHandler
from backend.groups import WidgetGroup
from pygame import event, mouse
from backend.util import salir
from .selected import Selected


class WidgetHandler:
    widgets = None
    observed_events = None

    selected = None

    @classmethod
    def init(cls):
        cls.widgets = WidgetGroup()
        cls.observed_events = [VIDEORESIZE, WINDOWRESTORED, WINDOWMAXIMIZED, WINDOWMINIMIZED, KEYDOWN, QUIT,
                               MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION]
        event.set_allowed(cls.observed_events)
        cls.selected = Selected()

    @classmethod
    def add_widget(cls, widget):
        if widget not in cls.widgets:
            cls.widgets.add(widget)

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
                for widget in cls.selected:
                    widget.on_key_down(e)

            elif e.type == KEYUP:
                pass

            elif e.type == MOUSEBUTTONDOWN:
                if e.button == 1:
                    widgets = [w for w in cls.widgets if w.rect.collidepoint(e.pos)]
                    for widget in widgets:
                        widget.is_pressed = True
                        if widget.is_selectable:
                            cls.selected.sumar(widget)

            elif e.type == MOUSEBUTTONUP:
                if e.button == 1:
                    widgets = [w for w in cls.widgets if w.is_pressed]
                    for widget in widgets:
                        widget.on_mousebutton_up(e)

            elif e.type == MOUSEMOTION:
                widgets = [w for w in cls.widgets if w.has_mouse_over]
                for widget in widgets:
                    widget.on_mousemotion(e)

            elif e.type == VIDEORESIZE:
                for widget in cls.widgets:
                    widget.on_video_resize(e)

            elif e.type == WINDOWRESTORED:
                for widget in cls.widgets:
                    widget.on_restore(e)

            elif e.type == WINDOWMAXIMIZED:
                for widget in cls.widgets:
                    widget.on_maximize(e)

            elif e.type == WINDOWMINIMIZED:
                for widget in cls.widgets:
                    widget.on_minimize(e)

        pos = mouse.get_pos()
        for widget in cls.widgets:
            if widget.rect.collidepoint(pos):
                widget.on_mouseover()
            else:
                widget.has_mouse_over = False

        cls.widgets.update()


EventHandler.register(lambda e: WidgetHandler.init(), 'Init')
