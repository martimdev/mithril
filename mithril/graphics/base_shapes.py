import math
from abc import ABC

import pygame
from pygame import gfxdraw
from pygame.rect import Rect

from mithril.graphics.shape import Shape


class HorizontalLine(Shape):
    def __init__(self, relative_x, relative_y, color, length):
        super().__init__(relative_x, relative_y, color)
        self.length = length

    def is_colliding(self, pos):
        return False

    def draw(self, screen):
        pygame.draw.line(screen, self.color,
                         (self.relative_x, self.relative_y),
                         (self.relative_x + self.length, self.relative_y)
                         )


class VerticalLine(Shape):
    def __init__(self, relative_x, relative_y, color, length):
        super().__init__(relative_x, relative_y, color)
        self.length = length

    def is_colliding(self, pos):
        return False

    def draw(self, screen):
        pygame.draw.line(screen, self.color,
                         (self.relative_x, self.relative_y),
                         (self.relative_x, self.relative_y + self.length)
                         )


class Polygon(Shape, ABC):
    def __init__(self, relative_x, relative_y, color, width, height):
        super().__init__(relative_x, relative_y, color)
        self.width = width
        self.height = height


class Rectangle(Polygon, Rect):
    def __init__(self, relative_x, relative_y, width, height, color):
        super().__init__(relative_x, relative_y, width, height, color)

    def is_colliding(self, pos):
        return self.collidepoint(pos[0], pos[1])

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self)
        for node in self.nodes:
            node.draw(screen)


class Circle(Shape):
    def __init__(self, relative_x, relative_y, color, border_color, radius):
        super().__init__(relative_x, relative_y, color)
        self.border_color = border_color
        self.radius = radius

    def is_colliding(self, pos):
        distance = math.hypot(pos[0] - self.relative_x, pos[1] - self.relative_y)
        return distance <= self.radius

    def update(self):
        super().update()

    def draw(self, screen):
        gfxdraw.filled_circle(screen, self.relative_x, self.relative_y, self.radius, self.color)
        gfxdraw.aacircle(screen, self.relative_x, self.relative_y, self.radius, self.border_color)
