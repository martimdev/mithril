from abc import ABC, abstractmethod


def mouse_empty_function(): pass


def keyboard_empty_function(event): pass


class Node(ABC):
    def __init__(self, relative_x, relative_y):
        self.parent = None
        self.x = relative_x
        self.y = relative_y
        self.relative_x = relative_x
        self.relative_y = relative_y
        self.selected = False
        self.nodes = []
        self.on_mouse_button_down = mouse_empty_function
        self.on_mouse_button_up = mouse_empty_function
        self.mouse_hover = False
        self.on_mouse_hover = mouse_empty_function
        self.on_mouse_enter = mouse_empty_function
        self.on_mouse_exit = mouse_empty_function
        self.on_mouse_left_click = mouse_empty_function
        self.on_mouse_middle_click = mouse_empty_function
        self.on_mouse_right_click = mouse_empty_function
        self.on_key_down = keyboard_empty_function
        self.on_key_up = keyboard_empty_function

    @abstractmethod
    def is_colliding(self, pos):
        pass

    @abstractmethod
    def draw(self, screen):
        pass

    def has_parent(self):
        return self.parent is not None

    def get_supreme_parent(self):
        if self.has_parent():
            if self.parent.has_parent():
                return self.parent.get_supreme_parent()
            else:
                return self.parent

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
