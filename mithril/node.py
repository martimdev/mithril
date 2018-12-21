import pygame
from pygame import Rect


class Node(Rect):
    def __init__(self, color, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = color
        self.sub_nodes = []

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self)
        for sub_node in self.sub_nodes:
            sub_node.draw(screen)

    def add_sub_node(self, sub_node):
        self.sub_nodes.append(sub_node)

    def move(self, x, y):
        self.move_ip(x, y)
        for sub_node in self.sub_nodes:
            sub_node.rect.move_ip(x, y)

    def move_to(self, x, y):
        self.x = x
        self.y = y
        for sub_node in self.sub_nodes:
            sub_node.rect.x = sub_node.x + x
            sub_node.rect.y = sub_node.y + y


class SubNode:
    def __init__(self, color, x, y, width, height, parent):
        self.parent = parent
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.sub_nodes = []
        self.rect = Node(
            color,
            self.parent.x + self.x,
            self.parent.y + self.y,
            self.width,
            self.height
        )

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        for sub_node in self.sub_nodes:
            sub_node.draw(screen)

    def add_sub_node(self, sub_node):
        self.sub_nodes.append(sub_node)
