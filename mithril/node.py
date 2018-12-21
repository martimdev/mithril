import pygame
from pygame import Rect


class Node:
    def __init__(self, color, x, y, width, height, parent=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.nodes = []
        if parent is None:
            self.rect = Rect(
                self.x,
                self.y,
                self.width,
                self.height
            )
        else:
            self.rect = Rect(
                parent.x + self.x,
                parent.y + self.y,
                self.width,
                self.height
            )

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self)
        for node in self.nodes:
            node.draw(screen)

    def add_node(self, sub_node):
        self.nodes.append(sub_node)

    def move(self, x, y):
        self.rect.move_ip(x, y)
        for node in self.nodes:
            node.rect.move_ip(x, y)

    def move_to(self, x, y):
        self.rect.x = x
        self.rect.y = y
        for node in self.nodes:
            node.rect.x = node.x + x
            node.rect.y = node.y + y
