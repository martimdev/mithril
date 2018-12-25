from mithril.controls.label import Label
from mithril.graphics.util_shapes import RoundedRectangle

DEFAULT_COLOR = (229, 229, 229)
DEFAULT_HOVER_COLOR = (233, 233, 233)
DEFAULT_BORDER_COLOR = (181, 181, 181)
DEFAULT_HOVER_BORDER_COLOR = (3, 158, 211)


class Button(RoundedRectangle):
    def __init__(self, name,
                 relative_x=0,
                 relative_y=0,
                 width=100,
                 height=30,
                 color=DEFAULT_COLOR,
                 radius=4
                 ):
        RoundedRectangle.__init__(self, relative_x, relative_y, color, width, height, radius)
        self.name = name
        self.label = Label(self.name)
        self.add_node(self.label)
        self.border.color = DEFAULT_BORDER_COLOR
        self.on_mouse_enter_handlers.append(self.mouse_enter_handler)
        self.on_mouse_exit_handlers.append(self.mouse_exit_handler)

    def mouse_enter_handler(self):
        self.color = DEFAULT_HOVER_COLOR
        self.border.color = DEFAULT_HOVER_BORDER_COLOR

    def mouse_exit_handler(self):
        self.color = DEFAULT_COLOR
        self.border.color = DEFAULT_BORDER_COLOR

    def update(self):
        super().update()
        self.label.relative_x = (self.width - self.label.get_width()) // 2
        self.label.relative_y = ((self.height - self.label.get_height()) // 2) - 1

    def draw(self, screen):
        super().draw(screen)
