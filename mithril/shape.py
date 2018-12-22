from abc import ABC

import pygame
from pygame import Rect
from mithril import Node


class Shape(Node, ABC):
    def __init__(self, relative_x, relative_y, width, height, color):
        super().__init__(relative_x, relative_y)
        self.width = width
        self.height = height
        self.color = color

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height


class Rectangle(Shape, Rect):
    def __init__(self, relative_x, relative_y, width, height, color):
        super().__init__(relative_x, relative_y, width, height, color)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self)
        for node in self.nodes:
            node.draw(screen)
