import math
from abc import ABC

import pygame
from pygame import Rect, gfxdraw

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


class RoundedRectangle(Shape):
    def __init__(self, relative_x, relative_y, color, width, height, radius):
        super().__init__(relative_x, relative_y, color)
        self.width = width
        self.height = height
        self.radius = radius
        self.rect1 = Rectangle(0, 0, 0, 0, 0)
        self.rect2 = Rectangle(0, 0, 0, 0, 0)
        self.circle1 = Circle(0, 0, 0, 0, self.radius)
        self.circle2 = Circle(0, 0, 0, 0, self.radius)
        self.circle3 = Circle(0, 0, 0, 0, self.radius)
        self.circle4 = Circle(0, 0, 0, 0, self.radius)
        self.add_node(self.circle1)
        self.add_node(self.circle2)
        self.add_node(self.circle3)
        self.add_node(self.circle4)
        self.add_node(self.rect1)
        self.add_node(self.rect2)

    def is_colliding(self, pos):
        default_nodes = [self.rect1, self.rect2, self.circle1, self.circle2, self.circle3, self.circle4]
        for node in default_nodes:
            if node.is_colliding(pos):
                return True

    def update(self):
        super().update()
        self.rect1.x = self.relative_x
        self.rect1.y = self.relative_y + self.radius
        self.rect1.width = self.width
        self.rect1.height = self.height - self.radius * 2
        self.rect1.color = self.color
        self.rect2.x = self.relative_x + self.radius
        self.rect2.y = self.relative_y
        self.rect2.width = self.width - self.radius * 2
        self.rect2.height = self.height
        self.rect2.color = self.color
        self.circle1.relative_x = self.relative_x + self.radius
        self.circle1.relative_y = self.relative_y + self.radius
        self.circle1.color = self.color
        self.circle1.border_color = self.color
        self.circle2.relative_x = self.relative_x - self.radius + self.width
        self.circle2.relative_y = self.relative_y + self.radius
        self.circle2.color = self.color
        self.circle2.border_color = self.color
        self.circle3.relative_x = self.relative_x + self.radius
        self.circle3.relative_y = self.relative_y - self.radius + self.height
        self.circle3.color = self.color
        self.circle3.border_color = self.color
        self.circle4.relative_x = self.relative_x - self.radius + self.width
        self.circle4.relative_y = self.relative_y - self.radius + self.height
        self.circle4.color = self.color
        self.circle4.border_color = self.color

    def draw(self, screen):
        for node in self.nodes:
            node.draw(screen)
