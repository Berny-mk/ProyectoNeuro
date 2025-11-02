import pygame
from bg import BG
from player import Player
from cambio_color import Cambio_Color
from obstaculos import (
    Obstaculo_rojo,
    Obstaculo_naranja,
    Obstaculo_celeste,
    Obstaculo_morado,
)
from fernando import Fernando
from colision import Colision, Colision_rect
from puntos import Puntos
from settings import Ancho, Alto, screen

class Game:
    def __init__(self):
        self.bg = [BG(0), BG(Alto)]
        self.player = Player(self)
        self.cambios = []
        self.speed = 1
        self.puntos = Puntos(hs=0)
        self.obstaculos_rojos = []
        self.obstaculos_naranjas = []
        self.obstaculos_celestes = []
        self.obstaculos_morados = []
        self.fernando = []
        self.collision = Colision()
        self.collision_rect = Colision_rect()
        self.playing = False
        self.set_label()

    def set_speed(self, loops):
        if loops % 1200 == 0:
            self.speed *= 1.5

    def aumentar_velocidad_horizontal(self, loops):
        if loops % 1000 == 0:
            for lista in [
                self.obstaculos_rojos,
                self.obstaculos_naranjas,
                self.obstaculos_celestes,
                self.obstaculos_morados,
            ]:
                for obstaculo in lista:
                    obstaculo.dx *= 1.2

    def set_label(self):
        big_font = pygame.font.SysFont("monospace", 24, bold=True)
        small_font = pygame.font.SysFont("monospace", 18)
        self.big_lbl = big_font.render(" G A M E  O V E R ", 1, (225, 225, 225))
        self.small_lbl = small_font.render("Press R to restart", 1, (225, 225, 225))

    def start(self):
        self.playing = True

    def over(self):
        screen.blit(self.big_lbl, (Ancho//2 - self.big_lbl.get_width()//2, Alto//4))
        screen.blit(self.small_lbl, (Ancho//2 - self.small_lbl.get_width()//2, Alto//2))
        self.playing = False

    # 🟢 Spawns
    def tospawn(self, loops):
        return loops % 2 == 0

    def spawn_cambios(self):
        y = self.cambios[-1].y - 500 if self.cambios else -250
        nuevo_cambio = Cambio_Color()
        nuevo_cambio.y = y
        self.cambios.append(nuevo_cambio)

    def spawn_obstaculos_rojos(self):
        y = self.obstaculos_rojos[-1].y - 250 if self.obstaculos_rojos else 140
        nuevo = Obstaculo_rojo()
        nuevo.y = y
        self.obstaculos_rojos.append(nuevo)

    def spawn_obstaculos_naranjas(self):
        y = self.obstaculos_naranjas[-1].y - 250 if self.obstaculos_naranjas else 140
        nuevo = Obstaculo_naranja()
        nuevo.y = y
        self.obstaculos_naranjas.append(nuevo)

    def spawn_obstaculos_celestes(self):
        y = self.obstaculos_celestes[-1].y - 250 if self.obstaculos_celestes else 140
        nuevo = Obstaculo_celeste()
        nuevo.y = y
        self.obstaculos_celestes.append(nuevo)

    def spawn_obstaculos_morados(self):
        y = self.obstaculos_morados[-1].y - 250 if self.obstaculos_morados else 140
        nuevo = Obstaculo_morado()
        nuevo.y = y
        self.obstaculos_morados.append(nuevo)

    def spawn_fernando(self):
        y = self.fernando[-1].y - 500 if self.fernando else -25
        nuevo = Fernando()
        nuevo.y = y
        self.fernando.append(nuevo)

    def restart(self):
        highscore = self.puntos.hs
        self.__init__()
        self.puntos.hs = highscore