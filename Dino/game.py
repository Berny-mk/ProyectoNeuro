import random
import pygame
from constants import WIDTH, HEIGHT, screen
from NeuroJump.bg import BG
from dino import Dino
from cactus import Cactus
from collision import Collision
from score import Score

class Game:
    def __init__(self, hs=0):
        self.bg = [BG(0), BG(WIDTH)]
        self.dino = Dino()
        self.obstacles = []
        self.collision = Collision()
        self.score = Score(hs)
        self.speed = 3
        self.playing = False
        self.set_label()
    
    def set_label(self):
        big_font = pygame.font.SysFont("monospace", 24, bold=True)
        small_font = pygame.font.SysFont("monospace", 18)
        self.big_lbl = big_font.render(" G A M E  O V E R ", True, (0, 0, 0))
        self.small_lbl = small_font.render("Press R to restart", True, (0, 0, 0))

    def start(self):
        self.playing = True

    def over(self):
        screen.blit(self.big_lbl, (WIDTH//2 - self.big_lbl.get_width()//2, HEIGHT//4))
        screen.blit(self.small_lbl, (WIDTH//2 - self.small_lbl.get_width()//2, HEIGHT//2))
        self.playing = False
    
    def tospawn(self, loops):
        return loops % 100 == 0

    def spawn_cactus(self):
        if len(self.obstacles) > 0:
            prev_cactus = self.obstacles[-1]
            x = random.randint(prev_cactus.x + self.dino.width + 84, WIDTH + prev_cactus.x + self.dino.width + 84)
        else:
            x = random.randint(WIDTH + 100, 1000)
        cactus = Cactus(x)
        self.obstacles.append(cactus)

    def restart(self):
        self.__init__(hs=self.score.hs)