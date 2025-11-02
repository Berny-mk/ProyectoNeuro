import pygame
from settings import Ancho, screen

class Puntos:
    def __init__(self, hs):
        self.hs = hs
        self.act = 0
        self.font = pygame.font.SysFont("monospace", 18)
        self.color = (255, 255, 255)

    def update(self):
        self.act += 1
        self.check_hs()

    def show(self):
        lbl = self.font.render(f"HI {self.hs}, {self.act}", 1, self.color)
        lbl_width = lbl.get_rect().width
        screen.blit(lbl, (Ancho - lbl_width - 10, 10))

    def check_hs(self):
        if self.act >= self.hs:
            self.hs = self.act

    def reset(self):
        self.act = 0