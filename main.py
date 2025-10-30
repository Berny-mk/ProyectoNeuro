import sys
import pygame
from game import Game
from constants import screen

def main():
    game = Game()
    dino = game.dino
    clock = pygame.time.Clock()
    loops = 0
    over = False

    while True:
        if game.playing:
            loops += 1

            for bg in game.bg:
                bg.update(-game.speed)
                bg.show()
            
            dino.update(loops)
            dino.show()

            if game.tospawn(loops):
                game.spawn_cactus()

            for cactus in game.obstacles:
                cactus.update(-game.speed)
                cactus.show()
                if game.collision.between(dino, cactus):
                    over = True                     
                if over:
                    game.over()
                    
            game.score.update(loops)
            game.score.show()    
            
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

if __name__ == "__main__":
    main()