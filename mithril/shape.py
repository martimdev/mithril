import math
from abc import ABC

import pygame
from pygame import Rect

from mithril import Node


class Shape(Node, ABC):
    def __init__(self, relative_x, relative_y, color):
        super().__init__(relative_x, relative_y)
        self.color = color


class Polygon(Shape, ABC):
    def __init__(self, relative_x, relative_y, color, width, height):
        super().__init__(relative_x, relative_y, color)
        self.width = width
        self.height = height

    def is_colliding(self, pos):
        return pos[0] in range(
            self.x,
            self.x + self.width
        ) and pos[1] in range(
            self.y,
            self.x + self.height
        )


class Rectangle(Polygon, Rect):
    def __init__(self, relative_x, relative_y, width, height, color):
        super().__init__(relative_x, relative_y, width, height, color)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self)
        for node in self.nodes:
            node.draw(screen)


class Circle(Shape):
    def __init__(self, relative_x, relative_y, color, radius):
        super().__init__(relative_x, relative_y, color)
        self.radius = radius

    def is_colliding(self, pos):
        distance = math.hypot(pos[0] - self.x, pos[1] - self.y)
        return distance <= self.radius

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.relative_x, self.relative_y), self.radius)
