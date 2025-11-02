import random
import pygame
from settings import screen, rojo, naranja, morado, celeste, colores

class Player:
    def __init__(self, game):
        self.game = game
        self.x = 180
        self.y = 500
        self.dy = 4
        self.gravity = 1.2
        self.onground = True
        self.jumping = False
        self.falling = False
        self.radio = 10
        self.color_actual = rojo
        self.color = self.color_actual
        self.set_texture()

    def update(self, loops):
        if self.jumping:
            self.y -= self.dy
            if self.y <= self.jump_stop:
                self.fall()
        elif self.falling:
            self.y += self.gravity * self.dy
            if self.y >= 640:
                self.game.over()
                return True

    def show(self):
        pygame.draw.circle(screen, self.color, (self.x, int(self.y)), self.radio)

    def set_texture(self):
        opciones = [c for c in colores if c != self.color]
        if opciones:
            nuevo_color = random.choice(opciones)
            self.color = nuevo_color
            self.color_actual = nuevo_color

    def get_color(self):
        if self.color_actual == rojo:
            return "rojo"
        elif self.color_actual == naranja:
            return "naranja"
        elif self.color_actual == morado:
            return "morado"
        elif self.color_actual == celeste:
            return "celeste"
        return "desconocido"

    def jump(self):
        self.jumping = True
        self.jump_stop = self.y - 70

    def fall(self):
        self.falling = True
        self.jumping = False

    def stop(self):
        self.falling = False
        self.onground = True
        self.y = 550