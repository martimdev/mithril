import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP


def mouse_button_down_handler(nodes):
    for node in nodes:
        if node.is_colliding(pygame.mouse.get_pos()):
            node.on_mouse_button_down()
            mouse_button_down_handler(node.nodes)


def mouse_button_up_handler(nodes):
    for node in nodes:
        if node.is_colliding(pygame.mouse.get_pos()):
            node.on_mouse_button_up()
            mouse_button_up_handler(node.nodes)


class Application:
    def __init__(self, title, resolution, scene):
        self.title = title
        self.resolution = resolution
        self.scene = scene
        self.screen = pygame.display.set_mode(self.resolution)
        self.running = False
        self.background_color = ()
        pygame.init()

    def update_scene(self):
        self.clear()
        for node in self.scene.nodes:
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
                    mouse_button_up_handler(self.scene.nodes)
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
