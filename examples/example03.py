# Importing Application, Scene and Button
from mithril import Application, Scene
from mithril.controls.button import Button
from mithril.colors import WHITE

# Creating a empty scene
scene = Scene()

# Creating a application with a created scene
app = Application("Example03", (640, 512), scene)

# Creating a basic button
button = Button('Button', 100, 100)

# Handling click event
button.on_mouse_button_up = lambda: print('Clicked')

# Adding button to scene
scene.add_node(button)

# Setting background color
app.set_background_color(WHITE)
# Running application
app.run()
