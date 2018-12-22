from mithril import Node
from mithril.colors import BLACK


class Label(Node):
    def __init__(self, relative_x, relative_y, font, text):
        super().__init__(relative_x, relative_y)
        self.color = BLACK
        self.surface = font.render(text, True, self.color)

    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))

    def get_width(self):
        return self.surface.get_width()

    def get_height(self):
        return self.surface.get_height()

    def is_colliding(self, pos):
        return pos[0] in range(
            self.x,
            self.x + self.get_width()
        ) and pos[1] in range(
            self.y,
            self.x + self.get_height()
        )
