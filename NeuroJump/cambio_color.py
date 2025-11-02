import os
import pygame
from settings import screen

class Cambio_Color:
    def __init__(self):
        self.width = 20
        self.height = 20
        self.x = 170
        self.y = -100
        self.angle = 0
        self.set_texture()
        self.show()

    def update(self, dy):
        self.y += dy
        self.angle = (self.angle + 1) % 360

    def show(self):
        rotated_image = pygame.transform.rotate(self.texture, self.angle)
        rect = rotated_image.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(rotated_image, rect.topleft)

    def set_texture(self):
        current_dir = os.path.dirname(__file__)
        path = os.path.join(current_dir, "assets", "colores.png")
        self.texture = pygame.image.load(path)
        self.texture = pygame.transform.scale(self.texture, (self.width, self.height))