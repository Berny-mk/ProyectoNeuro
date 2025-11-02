import os
import pygame
from settings import screen

class Fernando:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = 160
        self.y = -100
        self.set_texture()
        self.show()

    def update(self, dy):
        self.y += dy

    def show(self):
        screen.blit(self.texture, (self.x, self.y))

    def set_texture(self):
        current_dir = os.path.dirname(__file__)
        path = os.path.join(current_dir, "assets", "fernando.png")
        self.texture = pygame.image.load(path)
        self.texture = pygame.transform.scale(self.texture, (self.width, self.height))