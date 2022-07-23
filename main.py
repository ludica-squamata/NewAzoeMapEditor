from frontend.globales import Renderer, WidgetHandler
from backend.eventhandler import EventHandler

Renderer.init()
EventHandler.trigger('Init', 'System', {})

while True:
    EventHandler.process()
    WidgetHandler.update()
    Renderer.update()
