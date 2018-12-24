from mithril import Node


class Border(Node):
    def __init__(self, relative_x, relative_y, width, color):
        super().__init__(relative_x, relative_y)
        self.width = width
        self.color = color

    def is_colliding(self, pos):
        return False

    def draw(self, screen):
        for node in self.nodes:
            node.draw(screen)
