import pygame
from mithril import Node
from pygame import Rect


class Rectangle(Node, Rect):
    def __init__(self, color, x, y, width, height):
        super().__init__(color, x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self)
        for node in self.nodes:
            node.draw(screen)
