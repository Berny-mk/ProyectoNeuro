import os
import pygame
from constants import screen

class Cactus:
    def __init__(self, x):
        self.width = 34
        self.height = 44
        self.x = x
        self.y = 80
        self.set_texture()
        self.show()

    def update(self, dx):
        self.x += dx

    def show(self):
        screen.blit(self.texture, (self.x, self.y))

    def set_texture(self):
        path = os.path.join(os.path.dirname(__file__), "assets/cactus.png")
        self.texture = pygame.image.load(path)
        self.texture = pygame.transform.scale(self.texture, (self.width, self.height))