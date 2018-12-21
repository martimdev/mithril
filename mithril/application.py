import pygame
from pygame.locals import QUIT


class Application:
    def __init__(self, title, resolution):
        self.title = title
        self.resolution = resolution
        self.screen = pygame.display.set_mode(self.resolution)
        self.running = False

    def loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

    def run(self):
        pygame.init()
        self.running = True
        self.loop()

    def exit(self):
        self.running = False
