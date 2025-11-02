import pygame
import math

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