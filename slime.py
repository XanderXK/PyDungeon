import pygame
import animation_creator
from pygame import SurfaceType
import game_objects

class Slime:
    hp = 3

    def __init__(self, start_position):
        game_objects.add_slime(self)
        self.rect = pygame.Rect(0, 0, 50, 50)
        self.rect.center = start_position
        self.simple_animation = animation_creator.create_slime_animation()

    def draw(self, surface: SurfaceType):
        anim_frame = self.simple_animation.get_frame()
        surface.blit(anim_frame, self.rect)
        pygame.draw.rect(surface, (255, 255, 255), self.rect, 1)

    def update(self):
        a = 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            game_objects.remove_slime(self)
