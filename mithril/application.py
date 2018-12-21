import pygame
from pygame.locals import QUIT


class Application:
    def __init__(self, title, resolution, scene):
        self.title = title
        self.resolution = resolution
        self.scene = scene
        self.screen = pygame.display.set_mode(self.resolution)
        self.running = False

    def change_scene(self):
        for node in self.scene.nodes:
            node.draw(self.screen)

    def loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
            pygame.display.update()

    def run(self):
        pygame.init()
        pygame.display.set_caption(self.title)
        self.running = True
        self.loop()

    def exit(self):
        self.running = False
