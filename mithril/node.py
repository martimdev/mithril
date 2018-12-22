from abc import ABC, abstractmethod


def empty_function(): pass


class Node(ABC):
    def __init__(self, color, relative_x, relative_y, width, height):
        self.parent = None
        self.x = relative_x
        self.y = relative_y
        self.relative_x = relative_x
        self.relative_y = relative_y
        self.width = width
        self.height = height
        self.color = color
        self.nodes = []
        self.on_mouse_button_down = empty_function
        self.on_mouse_button_up = empty_function

    @abstractmethod
    def draw(self, screen):
        return

    def add_node(self, node):
        node.parent = self
        self.nodes.append(node)

    def move_to(self, x, y):
        self.x = x
        self.y = y
        for node in self.nodes:
            node.x = node.x + x
            node.y = node.y + y

    def is_colliding(self, pos):
        return pos[0] in range(
            self.x,
            self.x + self.width
        ) and pos[1] in range(
            self.y,
            self.x + self.height
        )
