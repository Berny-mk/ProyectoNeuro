import sys
import random
import pygame
import os
import math

WIDTH = 623
HEIGHT = 150

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Game")

class BG:
    def __init__(self,x):
        self.width = WIDTH
        self.height = HEIGHT
        self.x = x
        self.y = 0
        self.set_texture()
        self.show()
    
    def update(self, dx):
        self.x += dx
        if self.x <= -WIDTH:
            self.x = WIDTH

    def show(self):
        screen.blit(self.texture, (self.x,self.y))

    def set_texture(self):
        path = os.path.join(os.path.dirname(__file__), "bg.png")
        self.texture = pygame.image.load(path)
        self.texture = pygame.transform.scale(self.texture, (self.width, self.height))

class Dino:
    def __init__ (self):
        self.width = 44
        self.height = 44
        self.x = 10
        self.y = 80
        self.texture_num = 0
        self.dy = 3 
        self.gravity = 1.2
        self.onground = True
        self.jumping = False
        self.jump_stop = 10
        self.falling = False
        self.fall_stop = self.y
        self.set_texture()
        self.show()

    def update (self, loops):
        if self.jumping:
            self.y -= self.dy
            if self.y <= self.jump_stop:
                self.fall()

        elif self.falling:
            self.y += self.gravity*self.dy
            if self.y >= self.fall_stop:
                self.stop()
        else:    
        #walking:
            if loops %4 ==0:
                self.texture_num = (self.texture_num + 1) % 3
                self.set_texture()
    
    def show (self):
        screen.blit(self.texture, (self.x,self.y))

    
    def set_texture(self):
        path = os.path.join(os.path.dirname(__file__), f"dino{self.texture_num}.png")
        self.texture = pygame.image.load(path)
        self.texture = pygame.transform.scale(self.texture, (self.width, self.height))

    def jump (self):
        self.jumping = True
        self.onground = False

    def fall (self):
        self.falling = True
        self.jumping = False
    
    def stop(self):
        self.falling = False
        self.onground = True

class Cactus: 
    def __init__(self,x):
        self.width = 34
        self.height = 44
        self.x = x
        self.y = 80
        self.set_texture()
        self.show()


    def update(self, dx):
        self.x += dx

    def show(self):
        screen.blit(self.texture, (self.x,self.y))

    def set_texture(self):
        path = os.path.join(os.path.dirname(__file__), "cactus.png")
        self.texture = pygame.image.load(path)
        self.texture = pygame.transform.scale(self.texture, (self.width, self.height))

class Colission:
    def between(self, obj1, obj2):
        distance = math.sqrt((obj1.x - obj2.x) ** 2 + (obj1.y - obj2.y) ** 2) 
        return distance < 35

class Score:
    def __init__(self, hs):
        self.hs = hs
        self.act = 0
        self.font = pygame.font.SysFont("monospace", 18)
        self.color = (0, 0, 0)
    
    def update(self, loops):
        self.act = loops//10
        self.check_hs()

    def show(self):
        self.lbl = self.font.render(f"HI {self.hs}, {self.act}",100, self.color)
        lbl_width = self.lbl.get_rect().width
        screen.blit(self.lbl, (WIDTH - lbl_width - 10, 10))
    
    def check_hs(self):
        if self.act >= self.hs:
            self.hs = self.act
    
    def reset (self):
        self.act = 0
            
class Game:
    def __init__(self, hs = 0):
        self.bg = [BG(0), BG(WIDTH)]
        self.dino = Dino()
        self.obstacles = []
        self.collision = Colission()
        self.score = Score(hs)
        self.speed = 3
        self.playing = False
        self.set_label()
    
    def set_label(self):
        big_font = pygame.font.SysFont("monospace", 24, bold = True)
        small_font = pygame.font.SysFont("monospace", 18)
        self.big_lbl = big_font.render(f" G A M E  O V E R ", 1, (0, 0, 0))
        self.small_lbl = small_font.render(f"Press R to restart", 1, (0, 0, 0))


    def start (self):
        self.playing = True

    def over (self):
        screen.blit(self.big_lbl, (WIDTH//2 - self.big_lbl.get_width()//2, HEIGHT//4))
        screen.blit(self.small_lbl, (WIDTH//2 - self.small_lbl.get_width()//2, HEIGHT//2))
        self.playing = False
    
        
    def tospawn(self, loops):
        return loops % 100 == 0 

    def spawn_cactus(self):
        #List with cactus:
        if len(self.obstacles) > 0:
            prev_cactus = self.obstacles[-1]
            x = random.randint(prev_cactus.x + self.dino.width +84, WIDTH + prev_cactus.x + self.dino.width + 84)
        
        #empty list
        else:
            x = random.randint(WIDTH +100,1000)
        cactus = Cactus(x)
        self.obstacles.append(cactus)

    def restart(self):
        self.__init__(hs = self.score.hs)

def main(): 
    ## Objects
    game = Game()
    dino = game.dino

    clock = pygame.time.Clock()

    loops = 0 
    over = False

    # Main loop
    while True:
        if game.playing:

            loops += 1

            ## ----BG------
            for bg in game.bg:
                bg.update(-game.speed)
                bg.show()
            
            ## ----DINO------
            dino.update(loops)
            dino.show()

            ## ----CACTUS------
            if game.tospawn(loops):
                game.spawn_cactus()

            for cactus in game.obstacles:
                cactus.update(-game.speed)
                cactus.show()

                # Check for collision
                if game.collision.between(dino, cactus):
                    over = True                     
                
                if over:
                    game.over()
                    
            ## ----SCORE------
            game.score.update(loops)
            game.score.show()    
            
        ## ----Events------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not over:
                        if dino.onground:
                            dino.jump()
                        
                        if not game.playing:
                            game.start()

                if event.key == pygame.K_r:
                    game.restart()
                    dino = game.dino
                    loops = 0
                    over = False
            
        clock.tick(60) 
        pygame.display.update()

main()