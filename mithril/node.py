from abc import ABC, abstractmethod


def empty_function(): pass


class Node(ABC):
    def __init__(self, relative_x, relative_y):
        self.parent = None
        self.x = relative_x
        self.y = relative_y
        self.relative_x = relative_x
        self.relative_y = relative_y
        self.nodes = []
        self.on_mouse_button_down = empty_function
        self.on_mouse_button_up = empty_function
        self.mouse_hover = False
        self.on_mouse_hover = empty_function
        self.on_mouse_enter = empty_function
        self.on_mouse_exit = empty_function

    @abstractmethod
    def get_width(self):
        pass

    @abstractmethod
    def get_height(self):
        pass

    @abstractmethod
    def draw(self, screen):
        pass

    def has_parent(self):
        return self.parent is not None

    def update(self):
        if self.has_parent():
            self.x = self.parent.x + self.relative_x
            self.y = self.parent.y + self.relative_y
        for node in self.nodes:
            node.update()

    def add_node(self, node):
        node.parent = self
        self.nodes.append(node)

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def is_colliding(self, pos):
        return pos[0] in range(
            self.x,
            self.x + self.get_width()
        ) and pos[1] in range(
            self.y,
            self.x + self.get_height()
        )
