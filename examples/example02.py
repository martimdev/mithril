# Importing Application, Scene and Rectangle
from mithril import Application, Scene
from mithril.graphics.base_shapes import Rectangle

# Creating a empty scene
scene = Scene()

# Creating a 100 x 50 white rectangle
rect = Rectangle(100, 100, 100, 50, (255, 255, 255))

# Adding rectangle to scene
scene.add_node(rect)

# Creating a application with a created scene
app = Application("Example02", (1280, 720), scene)

# Running application
app.run()
