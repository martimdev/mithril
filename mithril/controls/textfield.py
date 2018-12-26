import datetime

import pygame

from mithril.controls.label import Label
from mithril.graphics.base_shapes import VerticalLine
from mithril.graphics.util_shapes import RoundedRectangle

DEFAULT_COLOR = (255, 255, 255)
DEFAULT_BORDER_COLOR = (181, 181, 181)
DEFAULT_HOVER_BORDER_COLOR = (3, 158, 211)


class TextField(RoundedRectangle):
    def __init__(self, text='',
                 relative_x=0,
                 relative_y=0,
                 width=150,
                 height=26,
                 color=DEFAULT_COLOR,
                 caret_size=14,
                 caret_color=(0, 0, 0),
                 caret_show_time=0.5,
                 spacing=5,
                 radius=4
                 ):
        super().__init__(relative_x, relative_y, color, width, height, radius)
        self.border.color = DEFAULT_BORDER_COLOR
        self.text = text
        self.caret_show_time = caret_show_time
        self.caret_size = caret_size
        self.caret_color = caret_color
        self.spacing = spacing
        self.caret_showing = False
        self.caret_timer = datetime.datetime.utcnow() + datetime.timedelta(seconds=self.caret_show_time)
        self.label = Label(self.text)
        self.caret = VerticalLine(0, 0, 0, 0)
        self.add_node(self.label)
        self.add_node(self.caret)
        self.on_key_down_handlers.append(self.key_down_handler)
        self.on_mouse_enter_handlers.append(self.mouse_enter_handler)
        self.on_mouse_exit_handlers.append(self.mouse_exit_handler)

    def mouse_enter_handler(self):
        self.border.color = DEFAULT_HOVER_BORDER_COLOR

    def mouse_exit_handler(self):
        self.border.color = DEFAULT_BORDER_COLOR

    def key_down_handler(self, event):
        if event.key == pygame.K_BACKSPACE:
            self.delete_last_char()
        else:
            self.write_char(event.unicode)

    def delete_last_char(self):
        self.label.text = self.label.text[:-1]
        self.text = self.text[:-1]
        if self.width > self.label.get_width() + self.spacing and len(self.text) > len(self.label.text):
            lent = len(self.text) - len(self.label.text)
            self.label.text = self.text[lent - 1:]

    def write_char(self, char):
        self.label.text += char
        self.text += char

    def update(self):
        super().update()
        print(self.caret_showing)
        if self.label.get_width() + self.spacing > self.width:
            self.label.text = self.label.text[1:]
        if datetime.datetime.utcnow() > self.caret_timer:
            self.caret_timer = datetime.datetime.utcnow() + datetime.timedelta(seconds=self.caret_show_time)
            self.caret_showing = not self.caret_showing
        self.label.relative_x = self.spacing
        self.label.relative_y = ((self.height - self.label.get_height()) // 2) - 1
        self.caret = VerticalLine(self.relative_x + self.spacing + self.label.get_width(),
                                  self.relative_y + (self.height - self.caret_size) // 2,
                                  self.caret_color,
                                  self.caret_size
                                  )

    def draw(self, screen):
        super().draw(screen)
        if self.caret_showing:
            self.caret.draw(screen)
