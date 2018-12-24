from abc import ABC, abstractmethod


class Node(ABC):
    def __init__(self, relative_x, relative_y):
        self.parent = None
        self.x = relative_x
        self.y = relative_y
        self.relative_x = relative_x
        self.relative_y = relative_y
        self.selected = False
        self.nodes = []
        self.on_mouse_button_down_handlers = []
        self.on_mouse_button_up_handlers = []
        self.mouse_hover = False
        self.on_mouse_hover_handlers = []
        self.on_mouse_enter_handlers = []
        self.on_mouse_exit_handlers = []
        self.on_mouse_left_click_handlers = []
        self.on_mouse_middle_click_handlers = []
        self.on_mouse_right_click_handlers = []
        self.on_key_down_handlers = []
        self.on_key_up_handlers = []

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
            self.x = self.parent.relative_x + self.relative_x
            self.y = self.parent.relative_y + self.relative_y
        for node in self.nodes:
            node.update()

    def add_node(self, node):
        node.parent = self
        self.nodes.append(node)

    def move_to(self, x, y):
        self.x = x
        self.y = y
