from pygame.sprite import LayeredUpdates
from backend.eventhandler import EventHandler


class Selected(LayeredUpdates):

    def sumar(self, *sprites):
        super().add(sprites)
        for sprite in sprites:
            sprite.select()
            EventHandler.trigger('select', self, {'target': sprite})

    def empty(self):
        for sprite in self.sprites():
            sprite.deselect()
            EventHandler.trigger('deselect', self, {'target': sprite})
        super().empty()
