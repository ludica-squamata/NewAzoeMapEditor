from frontend.globales import Renderer, WidgetHandler
from backend.eventhandler import EventHandler

EventHandler.trigger('Init', 'System', {})

while True:
    EventHandler.process()
    WidgetHandler.update()
    Renderer.update()
