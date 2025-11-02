import sys
import pygame
from game import Game

def main():
    pygame.init()
    clock = pygame.time.Clock()
    game = Game()
    player = game.player
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
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
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

                # Colisión con cambio de color
                if game.collision.between(player, cambio, 25):
                    player.set_texture()
                    game.cambios.remove(cambio)

            # Obstáculos (de cada color)
            if game.tospawn(loops):
                game.spawn_obstaculos_rojos()
                game.spawn_obstaculos_naranjas()
                game.spawn_obstaculos_celestes()
                game.spawn_obstaculos_morados()

            for lista, color_name in [
                (game.obstaculos_rojos, "rojo"),
                (game.obstaculos_naranjas, "naranja"),
                (game.obstaculos_celestes, "celeste"),
                (game.obstaculos_morados, "morado"),
            ]:
                for obstaculo in lista:
                    obstaculo.update(game.speed)
                    obstaculo.show()

                    # Colisión jugador–obstáculo
                    if game.collision_rect.between(player, obstaculo):
                        if player.get_color() == color_name:
                            continue
                        else:
                            game.playing = False

            # Fernando
            if game.tospawn(loops):
                game.spawn_fernando()

            for fernando in game.fernando[:]:
                fernando.update(game.speed)
                fernando.show()
                if game.collision.between(player, fernando, 50):
                    game.puntos.update()
                    game.fernando.remove(fernando)

            # Puntos
            game.puntos.show()

        # Eventos generales
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                player.jump()

        # Jugador
        player.show()

        # Render final
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()