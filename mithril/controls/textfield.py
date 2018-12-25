from mithril.controls.label import Label
from mithril.graphics.util_shapes import RoundedRectangle

DEFAULT_COLOR = (255, 255, 255)
DEFAULT_BORDER_COLOR = (181, 181, 181)
DEFAULT_HOVER_BORDER_COLOR = (3, 158, 211)


class TextField(RoundedRectangle):
    def __init__(self, text='',
                 relative_x=0,
                 relative_y=0,
                 width=150,
                 height=26,
                 color=DEFAULT_COLOR,
                 caret_size=14,
                 spacing=5,
                 radius=4
                 ):
        super().__init__(relative_x, relative_y, color, width, height, radius)
        self.border.color = DEFAULT_BORDER_COLOR
        self.text = text
        self.caret_size = caret_size
        self.spacing = spacing
        self.label = Label(self.text)
        self.add_node(self.label)
        self.on_key_down_handlers.append(self.key_down_handler)
        self.on_mouse_enter_handlers.append(self.mouse_enter_handler)
        self.on_mouse_exit_handlers.append(self.mouse_exit_handler)

    def mouse_enter_handler(self):
        self.border.color = DEFAULT_HOVER_BORDER_COLOR

    def mouse_exit_handler(self):
        self.border.color = DEFAULT_BORDER_COLOR

    def key_down_handler(self, event):
        self.write_char(event.unicode)

    def delete_last_char(self):
        self.label.text = self.label.text[:-1]
        self.text = self.text[:-1]

    def write_char(self, char):
        self.label.text += char
        self.text += char

    def update(self):
        super().update()
        self.label.relative_x = self.spacing
        self.label.relative_y = ((self.height - self.label.get_height()) // 2) - 1
        if self.label.get_width() + self.spacing > self.width:
            self.label.text = self.label.text[1:]

    def draw(self, screen):
        super().draw(screen)
