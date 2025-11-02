import sys
import random
import pygame
import os
import math

pygame.init()

## Pantalla:
Ancho = 360
Alto = 640
screen = pygame.display.set_mode((Ancho, Alto))
pygame.display.set_caption("Neuro Jump")

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
morado = (255, 0, 255)
rojo = (255, 0, 0)
naranja = (255, 128, 0)
celeste = (0, 255, 255)
colores = [morado, rojo, naranja, celeste]

#Clases:
class BG:
    def __init__ (self,y):
        self.width = Ancho
        self.height = Alto
        self.y = y
        self.x = 0
        self.set_texture()
        self.show()
    
    def update (self, dy):
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

class Player:
    def __init__ (self, game):
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
            self.y += self.gravity*self.dy
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

    
    def jump (self):
        self.jumping = True
        self.jump_stop = self.y - 70

    def fall (self):
        self.falling = True
        self.jumping = False
    
    def stop(self):
        self.falling = False
        self.onground = True
        self.y = 550

class Cambio_Color:
    def __init__ (self):
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

class Obstaculo_rojo:
    def __init__ (self):
        self.width = 125
        self.height = 20
        self.x = 0
        self.y = -50 
        self.dx = 2
        self.speed = 1
        self.set_texture()

    def set_speed (self, loops):
        if loops % 1000 == 0:
            self.speed = self.speed*2
        return self.speed
    
    def set_texture(self):
        self.texture = pygame.Surface((self.width, self.height))
        self.texture.fill(rojo)

    def update(self, dy):
        self.y += dy
        self.x += self.dx

        if self.x > Ancho:
            self.x = -self.width
        elif self.x + self.width < 0:
            self.x = Ancho

    def show(self):
        screen.blit(self.texture, (self.x, self.y))

class Obstaculo_naranja:
    def __init__ (self):
        self.width = 125
        self.height = 20
        self.x = 125
        self.y = -50
        self.dx = 2  
        self.speed = 1
        self.set_texture()

    def set_speed (self, loops):
        if loops % 1000 == 0:
            self.speed = self.speed*2
        return self.speed
    
    def set_texture(self):
        self.texture = pygame.Surface((self.width, self.height))
        self.texture.fill(naranja)

    def update(self, dy):
        self.y += dy
        self.x += self.dx

        if self.x > Ancho:
            self.x = -self.width
        elif self.x + self.width < 0:
            self.x = Ancho

    def show(self):
        screen.blit(self.texture, (self.x, self.y))

class Obstaculo_celeste:
    def __init__ (self):
        self.width = 125
        self.height = 20
        self.x = 250
        self.y = -50 
        self.dx = 2
        self.speed = 1
        self.set_texture()

    def set_speed (self, loops):
        if loops % 1000 == 0:
            self.speed = self.speed*2
        return self.speed
    

    def set_texture(self):
        self.texture = pygame.Surface((self.width, self.height))
        self.texture.fill(celeste)

    def update(self, dy):
        self.y += dy
        self.x += self.dx

        if self.x > Ancho:
            self.x = -self.width
        elif self.x + self.width < 0:
            self.x = Ancho

    def show(self):
        screen.blit(self.texture, (self.x, self.y))

class Obstaculo_morado:
    def __init__ (self):
        self.width = 125
        self.height = 20
        self.x = 375
        self.y = -50  
        self.dx = 2  
        self.speed = 1
        self.set_texture()

    def set_speed (self, loops):
        if loops % 1000 == 0:
            self.speed = self.speed*2
        return self.speed
    

    def set_texture(self):
        self.texture = pygame.Surface((self.width, self.height))
        self.texture.fill(morado)

    def update(self, dy):
        self.y += dy
        self.x += self.dx

        if self.x > Ancho:
            self.x = -self.width
        elif self.x + self.width < 0:
            self.x = Ancho

    def show(self):
        screen.blit(self.texture, (self.x, self.y))

class Fernando:
    def __init__ (self):
        self.width = 50
        self.height = 50
        self.x = 160
        self.y = -100
        self.set_texture()
        self.show()

    def update(self, dy):
        self.y += dy

    def show(self):
        screen.blit(self.texture, (self.x,self.y))

    def set_texture(self):
        current_dir = os.path.dirname(__file__)
        path = os.path.join(current_dir, "assets", "fernando.png")
        self.texture = pygame.image.load(path)
        self.texture = pygame.transform.scale(self.texture, (self.width, self.height))

class Colision: 
    def between(self, obj1, obj2, distancia):
        distance = math.hypot(obj1.x - obj2.x, obj1.y - obj2.y)
        return distance < distancia

class Colision_rect:
    def between(self, circle_obj, rect_obj):
        circle_hitbox = pygame.Rect(
            circle_obj.x - circle_obj.radio,
            circle_obj.y - circle_obj.radio,
            circle_obj.radio * 2,
            circle_obj.radio * 2
        )
        rect_hitbox = pygame.Rect(rect_obj.x, rect_obj.y, rect_obj.width, rect_obj.height)
        return circle_hitbox.colliderect(rect_hitbox)


class Puntos: 

    def __init__(self, hs):
        self.hs = hs
        self.act = 0
        self.font = pygame.font.SysFont("monospace", 18)
        self.color = (255, 255, 255)
    
    def update(self):
        self.act = self.act +1
        self.check_hs()

    def show(self):
        self.lbl = self.font.render(f"HI {self.hs}, {self.act}",1, self.color)
        lbl_width = self.lbl.get_rect().width
        screen.blit(self.lbl, (Ancho - lbl_width - 10, 10))
    
    def check_hs(self):
        if self.act >= self.hs:
            self.hs = self.act
    
    def reset (self):
        self.act = 0

class Game:
    def __init__(self):
        self.bg = [BG(0), BG(Alto)]
        self.player = Player(self)
        self.cambios = []
        self.speed = 1
        self.puntos = Puntos(hs = 0)
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
        if loops %  1200 == 0:
            self.speed = self.speed * 1.5
    
    def aumentar_velocidad_horizontal(self, loops):
        if loops % 1000 == 0:
            for obstaculo in self.obstaculos_rojos:
                obstaculo.dx *= 1.2
            for obstaculo in self.obstaculos_naranjas:
                obstaculo.dx *= 1.2
            for obstaculo in self.obstaculos_celestes:
                obstaculo.dx *= 1.2
            for obstaculo in self.obstaculos_morados:
                obstaculo.dx *= 1.2

    
    def set_label(self):
        big_font = pygame.font.SysFont("monospace", 24, bold = True)
        small_font = pygame.font.SysFont("monospace", 18)
        self.big_lbl = big_font.render(f" G A M E  O V E R ", 1, (225, 225, 225))
        self.small_lbl = small_font.render(f"Press R to restart", 1, (225, 225, 225))

    def start (self):
        self.playing = True

    def over (self):
        screen.blit(self.big_lbl, (Ancho//2 - self.big_lbl.get_width()//2, Alto//4))
        screen.blit(self.small_lbl, (Ancho//2 - self.small_lbl.get_width()//2, Alto//2))
        self.playing = False

    def tospawn(self, loops):
        return loops % 2 == 0
    
    def spawn_cambios(self):
        if len(self.cambios) > 0:
            prev_cambio = self.cambios[-1]
            y = prev_cambio.y - 500
        
        #empty list
        else:
            y = -250
        nuevo_cambio = Cambio_Color()
        nuevo_cambio.y = y
        self.cambios.append(nuevo_cambio)
    
    def spawn_obstaculos_rojos(self):
        if len(self.obstaculos_rojos) > 0:
            prev_obstaculo = self.obstaculos_rojos[-1]
            y = prev_obstaculo.y -250
        else:
            y = 140
        nuevo_obstaculo = Obstaculo_rojo()
        nuevo_obstaculo.y = y
        self.obstaculos_rojos.append(nuevo_obstaculo)
    
    def spawn_obstaculos_naranjas(self):
        if len(self.obstaculos_naranjas) > 0:
            prev_obstaculo = self.obstaculos_naranjas[-1]
            y = prev_obstaculo.y - 250
        else:
            y = 140
        nuevo_obstaculo = Obstaculo_naranja()
        nuevo_obstaculo.y = y
        self.obstaculos_naranjas.append(nuevo_obstaculo)
    
    def spawn_obstaculos_celestes(self):
        if len(self.obstaculos_celestes) > 0:
            prev_obstaculo = self.obstaculos_celestes[-1]
            y = prev_obstaculo.y - 250
        else:
            y = 140
        nuevo_obstaculo = Obstaculo_celeste()
        nuevo_obstaculo.y = y
        self.obstaculos_celestes.append(nuevo_obstaculo)
    
    def spawn_obstaculos_morados(self):
        if len(self.obstaculos_morados) > 0:
            prev_obstaculo = self.obstaculos_morados[-1]
            y = prev_obstaculo.y - 250
        else:
            y = 140
        nuevo_obstaculo = Obstaculo_morado()
        nuevo_obstaculo.y = y
        self.obstaculos_morados.append(nuevo_obstaculo)
    
    def spawn_fernando (self):
        if len(self.fernando) > 0:
            prev_fernando = self.fernando[-1]
            y = prev_fernando.y - 500
        else:
            y = -25
        nuevo_fernando = Fernando()
        nuevo_fernando.y = y
        self.fernando.append(nuevo_fernando)
    
    def restart(self):
        highscore = self.puntos.hs
        self.__init__()
        self.puntos.hs = highscore



def main():
    game = Game()
    player = game.player
    obst_rojo = Obstaculo_rojo()
    obst_naranja = Obstaculo_naranja()
    obst_celeste = Obstaculo_celeste()
    obst_morado = Obstaculo_morado()
    clock = pygame.time.Clock()
    loops = 0
    game.playing = True  
    while True:
        loops += 1

        if not game.playing:
            game.over()
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game.restart()
                        loops = 0
                        player = game.player
                        game.playing = True



            continue 

        if player.update(loops):
            game.playing = False

        else:
            game.set_speed(loops)
            game.aumentar_velocidad_horizontal(loops)


            # Fondo
            for bg in game.bg:
                bg.update(game.speed)
                bg.show()

            # Cambios de color
            if game.tospawn(loops):
                game.spawn_cambios()

            for cambio in game.cambios[:]: 
                cambio.update(game.speed)
                cambio.show()

                # Detectar colisión
                if game.collision.between(player, cambio, 25):
                    Player.set_texture(player)
                    game.cambios.remove(cambio) 

            # Obstáculos
            if game.tospawn(loops):
                game.spawn_obstaculos_rojos()
            if game.tospawn(loops):
                game.spawn_obstaculos_naranjas()
            if game.tospawn(loops):
                game.spawn_obstaculos_morados()
            if game.tospawn(loops):
                game.spawn_obstaculos_celestes()
            

            for obstaculo in game.obstaculos_rojos:
                obstaculo.update(game.speed)
                obstaculo.show()
                # Detectar colisión
                if game.collision_rect.between(player, obstaculo):
                    if player.get_color() == "rojo":
                        game.playing = True
                    else:
                        game.playing = False
            
                
            for obstaculo in game.obstaculos_naranjas:
                obstaculo.update(game.speed)
                obstaculo.show()
                # Detectar colisión
                if game.collision_rect.between(player, obstaculo):
                    if player.get_color() == "naranja":
                        game.playing = True
                    else:
                        game.playing = False
                
            for obstaculo in game.obstaculos_celestes:
                obstaculo.update(game.speed)
                obstaculo.show()
                # Detectar colisión
                if game.collision_rect.between(player, obstaculo):
                    if player.get_color() == "celeste":
                        game.playing = True
                    else:
                        game.playing = False
            
            for obstaculo in game.obstaculos_morados:
                obstaculo.update(game.speed)
                obstaculo.show()
                # Detectar colisión
                if game.collision_rect.between(player, obstaculo):
                    if player.get_color() == "morado":
                        game.playing = True
                    else:
                        game.playing = False

            # Fernando
            if game.tospawn(loops):
                game.spawn_fernando()

            for fernando in game.fernando[:]:
                fernando.update(game.speed)
                fernando.show()
            # Detectar colisión
                if game.collision.between(player, fernando, 50):
                    game.puntos.update()
                    game.fernando.remove(fernando)
            # Puntos
            
            game.puntos.show() 

            # Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        player.jump()

        player.show()
        pygame.display.flip()
        clock.tick(60)


main()
