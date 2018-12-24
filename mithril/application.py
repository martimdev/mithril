import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION, KEYDOWN, KEYUP


def mouse_button_down_handler(nodes):
    for node in nodes:
        if node.is_colliding(pygame.mouse.get_pos()):
            for handler in node.on_mouse_button_down_handlers:
                handler()
            mouse_button_down_handler(node.nodes)


def mouse_button_up_handler(scene, nodes, event):
    for node in nodes:
        if node.is_colliding(pygame.mouse.get_pos()):
            for handler in node.on_mouse_button_up_handlers:
                handler()
            if node.has_parent():
                scene.selected_node = node.get_supreme_parent()
            else:
                scene.selected_node = node
            if event.button == 1:
                for handler in node.on_mouse_left_click_handlers:
                    handler()
            elif event.button == 2:
                for handler in node.on_mouse_middle_click_handlers:
                    handler()
            elif event.button == 3:
                for handler in node.on_mouse_right_click_handlers:
                    handler()
            mouse_button_up_handler(scene, node.nodes, event)


def mouse_motion_handler(nodes):
    for node in nodes:
        if node.is_colliding(pygame.mouse.get_pos()):
            if not node.mouse_hover:
                node.mouse_hover = True
                for handler in node.on_mouse_enter_handlers:
                    handler()
            mouse_motion_handler(node.nodes)
        elif node.mouse_hover:
            node.mouse_hover = False
            for handler in node.on_mouse_exit_handlers:
                handler()


def mouse_hover_handler(nodes):
    for node in nodes:
        if node.mouse_hover:
            for handler in node.on_mouse_hover_handlers:
                handler()
            mouse_hover_handler(node.nodes)


def key_down_handler(scene, event):
    if scene.selected_node is not None:
        for handler in scene.selected_node.on_key_down_handlers:
            handler(event)


def key_up_handler(scene, event):
    if scene.selected_node is not None:
        for handler in scene.selected_node.on_key_up_handlers:
            handler(event)


class Application:
    def __init__(self, title, resolution, scene):
        self.title = title
        self.resolution = resolution
        self.scene = scene
        self.screen = pygame.display.set_mode(self.resolution)
        self.running = False
        self.background_color = (0, 0, 0)
        pygame.init()

    def update_scene(self):
        self.clear()
        for node in self.scene.nodes:
            node.update()
            node.draw(self.screen)

    def set_background_color(self, color):
        self.background_color = color
        self.screen.fill(color)

    def loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                if event.type == MOUSEBUTTONDOWN:
                    mouse_button_down_handler(self.scene.nodes)
                if event.type == MOUSEBUTTONUP:
                    mouse_button_up_handler(self.scene, self.scene.nodes, event)
                if event.type == MOUSEMOTION:
                    mouse_motion_handler(self.scene.nodes)
                if event.type == KEYDOWN:
                    key_down_handler(self.scene, event)
                if event.type == KEYUP:
                    key_up_handler(self.scene, event)

            mouse_hover_handler(self.scene.nodes)
            pygame.display.update()
            self.update_scene()

    def run(self):
        pygame.display.set_caption(self.title)
        self.running = True
        self.loop()

    def exit(self):
        self.running = False

    def clear(self):
        self.screen.fill(self.background_color)
