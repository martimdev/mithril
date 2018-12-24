from abc import ABC, abstractmethod

from mithril import Node


class Bordered(ABC):
    def __init__(self, border_color, border_width):
        self.border_color = border_color
        self.border_width = border_width

    @abstractmethod
    def draw_border(self, screen): pass


class Shape(Node, ABC):
    def __init__(self, relative_x, relative_y, color):
        super().__init__(relative_x, relative_y)
        self.color = color
