from mithril.graphics.shape import Shape
from mithril.graphics.base_shapes import Rectangle, Circle


class RoundedRectangle(Shape):
    def __init__(self, relative_x, relative_y, color, width, height, radius):
        super().__init__(relative_x, relative_y, color)
        self.width = width
        self.height = height
        self.radius = radius
        self.rect1 = Rectangle(0, 0, 0, 0, 0)
        self.rect2 = Rectangle(0, 0, 0, 0, 0)
        self.circle1 = Circle(0, 0, 0, 0, self.radius)
        self.circle2 = Circle(0, 0, 0, 0, self.radius)
        self.circle3 = Circle(0, 0, 0, 0, self.radius)
        self.circle4 = Circle(0, 0, 0, 0, self.radius)
        self.add_node(self.circle1)
        self.add_node(self.circle2)
        self.add_node(self.circle3)
        self.add_node(self.circle4)
        self.add_node(self.rect1)
        self.add_node(self.rect2)

    def is_colliding(self, pos):
        default_nodes = [self.rect1, self.rect2, self.circle1, self.circle2, self.circle3, self.circle4]
        for node in default_nodes:
            if node.is_colliding(pos):
                return True

    def update(self):
        super().update()
        self.rect1.x = self.relative_x
        self.rect1.y = self.relative_y + self.radius
        self.rect1.width = self.width
        self.rect1.height = self.height - self.radius * 2
        self.rect1.color = self.color
        self.rect2.x = self.relative_x + self.radius
        self.rect2.y = self.relative_y
        self.rect2.width = self.width - self.radius * 2
        self.rect2.height = self.height
        self.rect2.color = self.color
        self.circle1.relative_x = self.relative_x + self.radius
        self.circle1.relative_y = self.relative_y + self.radius
        self.circle1.color = self.color
        self.circle1.border_color = self.color
        self.circle2.relative_x = self.relative_x - self.radius + self.width - 1
        self.circle2.relative_y = self.relative_y + self.radius
        self.circle2.color = self.color
        self.circle2.border_color = self.color
        self.circle3.relative_x = self.relative_x + self.radius
        self.circle3.relative_y = self.relative_y - self.radius + self.height - 1
        self.circle3.color = self.color
        self.circle3.border_color = self.color
        self.circle4.relative_x = self.relative_x - self.radius + self.width - 1
        self.circle4.relative_y = self.relative_y - self.radius + self.height - 1
        self.circle4.color = self.color
        self.circle4.border_color = self.color

    def draw(self, screen):
        for node in self.nodes:
            node.draw(screen)
