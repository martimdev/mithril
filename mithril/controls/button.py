import pygame

from mithril.shape import RoundedRectangle
from mithril.controls.text import Label

DEFAULT_COLOR = (229, 229, 229)
DEFAULT_HOVER_COLOR = (233, 233, 233)
DEFAULT_BORDER_COLOR = (181, 181, 181)
DEFAULT_HOVER_BORDER_COLOR = (3, 158, 211)
DEFAULT_FONT_NAME = 'SEGOE UI'


class Button(RoundedRectangle):
    def __init__(self, name,
                 relative_x=0,
                 relative_y=0,
                 width=100,
                 height=30,
                 color=DEFAULT_COLOR,
                 border_color=DEFAULT_BORDER_COLOR,
                 radius=4
                 ):
        super().__init__(relative_x, relative_y, color, width, height, radius)
        self.name = name
        self.border_color = border_color
        self.label = Label(0, 0, pygame.font.SysFont(DEFAULT_FONT_NAME, 13), self.name)
        self.add_node(self.label)
        self.on_mouse_enter = self.mouse_enter_handler
        self.on_mouse_exit = self.mouse_exit_handler

    def mouse_enter_handler(self):
        self.color = DEFAULT_HOVER_COLOR
        self.border_color = DEFAULT_HOVER_BORDER_COLOR

    def mouse_exit_handler(self):
        self.color = DEFAULT_COLOR
        self.border_color = DEFAULT_BORDER_COLOR

    def update(self):
        super().update()
        self.circle1.border_color = self.border_color
        self.circle2.border_color = self.border_color
        self.circle3.border_color = self.border_color
        self.circle4.border_color = self.border_color
        self.label.relative_x = (self.width - self.label.get_width()) // 2
        self.label.relative_y = ((self.height - self.label.get_height()) // 2) - 1

    def draw(self, screen):
        super().draw(screen)
        pygame.draw.line(screen, self.border_color,
                         (self.relative_x + self.radius, self.relative_y),
                         (self.relative_x - self.radius + self.width, self.relative_y)
                         )
        pygame.draw.line(screen, self.border_color,
                         (self.relative_x + self.radius, self.relative_y + self.height),
                         (self.relative_x - self.radius + self.width, self.relative_y + self.height)
                         )
        pygame.draw.line(screen, self.border_color,
                         (self.relative_x, self.relative_y + self.radius),
                         (self.relative_x, self.relative_y - self.radius + self.height)
                         )
        pygame.draw.line(screen, self.border_color,
                         (self.relative_x + self.width, self.relative_y + self.radius),
                         (self.relative_x + self.width, self.relative_y - self.radius + self.height)
                         )
