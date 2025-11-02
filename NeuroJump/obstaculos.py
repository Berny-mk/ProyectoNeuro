import pygame
from settings import Ancho, screen, rojo, naranja, celeste, morado

class ObstaculoBase:
    def __init__(self, x, color):
        self.width = 125
        self.height = 20
        self.x = x
        self.y = -50
        self.dx = 2
        self.speed = 1
        self.color = color
        self.set_texture()

    def set_speed(self, loops):
        if loops % 1000 == 0:
            self.speed *= 2
        return self.speed

    def set_texture(self):
        self.texture = pygame.Surface((self.width, self.height))
        self.texture.fill(self.color)

    def update(self, dy):
        self.y += dy
        self.x += self.dx
        if self.x > Ancho:
            self.x = -self.width
        elif self.x + self.width < 0:
            self.x = Ancho

    def show(self):
        screen.blit(self.texture, (self.x, self.y))


class Obstaculo_rojo(ObstaculoBase):
    def __init__(self):
        super().__init__(x=0, color=rojo)


class Obstaculo_naranja(ObstaculoBase):
    def __init__(self):
        super().__init__(x=125, color=naranja)


class Obstaculo_celeste(ObstaculoBase):
    def __init__(self):
        super().__init__(x=250, color=celeste)


class Obstaculo_morado(ObstaculoBase):
    def __init__(self):
        super().__init__(x=375, color=morado)