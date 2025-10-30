import pygame
from constants import WIDTH, screen

class Score:
    def __init__(self, hs):
        self.hs = hs
        self.act = 0
        self.font = pygame.font.SysFont("monospace", 18)
        self.color = (0, 0, 0)
    
    def update(self, loops):
        self.act = loops // 10
        self.check_hs()

    def show(self):
        lbl = self.font.render(f"HI {self.hs}, {self.act}", True, self.color)
        lbl_width = lbl.get_rect().width
        screen.blit(lbl, (WIDTH - lbl_width - 10, 10))
    
    def check_hs(self):
        if self.act >= self.hs:
            self.hs = self.act
    
    def reset(self):
        self.act = 0