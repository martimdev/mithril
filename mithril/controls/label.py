from pygame.font import SysFont

from mithril import Node

DEFAULT_FONT_COLOR = (0, 0, 0)
DEFAULT_FONT_NAME = 'SEGOE UI'
DEFAULT_FONT_SIZE = 14


class Label(Node):
    def __init__(self, text,
                 relative_x=0,
                 relative_y=0,
                 font_color=DEFAULT_FONT_COLOR,
                 font_name=DEFAULT_FONT_NAME,
                 font_size=DEFAULT_FONT_SIZE,
                 ):
        super().__init__(relative_x, relative_y)
        self.text = text
        self.font_color = font_color
        self.font_name = font_name
        self.font_size = font_size
        self.font = SysFont(self.font_name, self.font_size)
        self.surface = self.font.render(self.text, True, self.font_color)

    def update(self):
        super().update()
        self.font = SysFont(self.font_name, self.font_size)
        self.surface = self.font.render(self.text, True, self.font_color)

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
