from frontend.widgets.buttons import ArrowButton, CloseTabButton, AddTabButton
from pygame import image, Surface, K_LEFT, K_RIGHT, K_UP, K_DOWN, Rect
from frontend.globales import raised_border, WidgetHandler
from frontend.widgets import BaseWidget, Tab
from os import getcwd, path, listdir


class MapArea(BaseWidget):
    maps = None
    tabs = None
    current = 0
    map_positions = None

    def __init__(self, parent, **pos):
        super().__init__(parent)
        self.image = raised_border(Surface((642, 482)))
        self.rect = self.image.get_rect(**pos)
        self.tabs = []
        self.map_positions = []
        self.arrow_left = ArrowButton(self, 'left', bottom=self.rect.top, left=self.rect.x)
        self.arrow_right = ArrowButton(self, 'right', bottom=self.rect.top, right=self.rect.right)
        dw = self.arrow_right.rect.w
        self.arrow_right.set_method(lambda: self.pan_tabs(+1))
        self.arrow_left.set_method(lambda: self.pan_tabs(-1))
        self.close_tab_button = CloseTabButton(self, right=self.arrow_right.rect.left, bottom=self.rect.top)
        self.close_tab_button.set_method(self.close_tab)
        dw += self.close_tab_button.rect.w
        self.add_tab_button = AddTabButton(self, right=self.close_tab_button.rect.left, bottom=self.rect.top)
        dw += self.add_tab_button.rect.w
        self.tab_area = Rect(self.arrow_left.rect.right + 1, self.arrow_left.rect.top, self.rect.w - dw - 18,
                             self.arrow_left.rect.h)
        self.tab_area_widget = TabArea(self, self.tab_area)
        ruta = path.join(getcwd(), 'data')
        w = self.tab_area.x
        for i, file in enumerate(listdir(ruta), start=1):
            filename = path.join(ruta, file)
            mapa = image.load(filename).convert_alpha()
            tb = Tab(self, 'Sin Título {}', i, mapa, bottom=self.rect.top, left=w)
            w = tb.rect.right + 3
            self.tabs.append(tb)
            self.map_positions.append([3, 3])
            if self.tab_area.contains(tb.rect):
                tb.show()
            else:
                tb.hide()

        self.update_arrow_status()
        self.show()

    def on_key_down(self, event):
        dx, dy = 0, 0
        if event.key == K_LEFT:
            dx = -10
        elif event.key == K_RIGHT:
            dx = 10
        if event.key == K_UP:
            dy = -10
        elif event.key == K_DOWN:
            dy = 10

        self.pan(dx, dy)

    def on_mousemotion(self, event):
        if self.has_mouse_over and self.is_pressed:
            self.pan(*event.rel)

    def on_mousebutton_up(self, event):
        if event.button == 1:
            self.is_pressed = False

    def pan(self, dx, dy):
        pos_x, pos_y = self.map_positions[self.current]
        if 3 >= pos_x + dx >= -161:
            self.map_positions[self.current][0] += dx
        if 3 >= pos_y + dy >= -321:
            self.map_positions[self.current][1] += dy

    def select_tab(self, tab):
        if tab in self.tabs:
            self.current = self.tabs.index(tab)

        for idx, tab in enumerate(self.tabs):
            if idx != self.current:
                tab.deselect()

    def pan_tabs(self, direction):
        for idx, tab in enumerate(self.tabs):
            tab.move(-direction)
            if not self.tab_area.contains(tab.rect):
                tab.hide()
            elif not tab.flagged:
                tab.show()

        self.update_arrow_status()

    def close_tab(self):
        idx = self.current
        tab = self.tabs[idx]
        tab.hide()
        tab.flagged = True
        if idx == 0:
            self.current = 1
        if idx >= len(self.tabs) - 1:
            self.current = 0
        else:
            self.current = idx + 1

        self.tabs[self.current].select()
        self.sort_tabs()

    def sort_tabs(self):
        x = self.tab_area.x - 3
        tabs = [tab for tab in self.tabs if not tab.flagged]
        for tab in tabs:
            tab.rect.x = x + 3
            x += tab.rect.w + 3
            if not self.tab_area.contains(tab.rect):
                tab.hide()
            elif not tab.is_visible:
                tab.show()

    def relocate_tabs(self, tab, dx):
        idx = self.tabs.index(tab)
        new_idx = None
        tabs = set(self.tabs) - {tab}
        agregated_w = 0
        for other_tab in sorted(tabs):
            agregated_w += other_tab.rect.w
            other_tab_index = self.tabs.index(other_tab)
            if dx < other_tab.rect.left:
                new_idx = other_tab_index - 1
                break
            elif dx > other_tab.rect.right:
                new_idx = other_tab_index + 1
        if dx < self.tab_area.left:
            new_idx = 0
        if dx > self.tab_area.right:
            new_idx = -1
        if new_idx != idx:
            del self.tabs[idx]
            self.tabs.insert(new_idx, tab)
            self.current = self.tabs.index(tab)
            for tab in self.tabs:
                tab.idx = self.tabs.index(tab)
        self.sort_tabs()

    def update_arrow_status(self):
        if self.tabs[0].is_visible:
            self.arrow_left.disable()
        else:
            self.arrow_left.enable()

        if self.tabs[-1].is_visible:
            self.arrow_right.disable()
        else:
            self.arrow_right.enable()

    def update(self):
        self.image.fill((0, 0, 0))
        mapa = self.tabs[self.current].linked_document
        self.image.blit(mapa, self.map_positions[self.current])
        self.image = raised_border(self.image)


class TabArea(BaseWidget):
    def __init__(self, parent, rect):
        super().__init__(parent)
        self.rect = rect
        WidgetHandler.add_widget(self)

    def on_mousebutton_down(self, event):
        if event.button == 4:
            if self.parent.arrow_left.is_enabled:
                self.parent.arrow_left.method()
        elif event.button == 5:
            if self.parent.arrow_right.is_enabled:
                self.parent.arrow_right.method()
