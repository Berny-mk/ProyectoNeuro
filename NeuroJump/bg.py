import os
import pygame
from settings import Ancho, Alto, screen

class BG:
    def __init__(self, y):
        self.width = Ancho
        self.height = Alto
        self.y = y
        self.x = 0
        self.set_texture()
        self.show()

    def update(self, dy):
        self.y += dy
        if self.y >= Alto:
            self.y -= 2 * self.height

    def show(self):
        screen.blit(self.texture, (self.x, self.y))

    def set_texture(self):
        current_dir = os.path.dirname(__file__)
        path = os.path.join(current_dir, "assets", "fondo.png")
        self.texture = pygame.image.load(path)
        self.texture = pygame.transform.scale(self.texture, (self.width, self.height))