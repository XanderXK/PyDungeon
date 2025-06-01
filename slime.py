import math
import pygame
import animation_creator
import game_objects
from pygame import SurfaceType


class Slime:
    _hp = 2
    _speed = 3
    _damage = 1

    def __init__(self, start_position):
        game_objects.add_slime(self)
        self.rect = pygame.Rect(0, 0, 50, 50)
        self.rect.center = start_position
        self.simple_animation = animation_creator.create_slime_animation()

    def draw(self, screen: SurfaceType):
        anim_frame = self.simple_animation.get_frame()
        screen.blit(anim_frame, self.rect)

    def update(self):
        self.move_to_player()
        self.try_deal_damage()

    def move_to_player(self):
        player_rect = game_objects.player.rect
        x_distance = player_rect.centerx - self.rect.centerx
        y_distance = -(player_rect.centery - self.rect.centery)
        angle = math.degrees(math.atan2(y_distance, x_distance))
        dx = math.cos(math.radians(angle)) * self._speed
        dy = -math.sin(math.radians(angle)) * self._speed
        self.rect.centerx += dx
        self.rect.centery += dy

    def take_damage(self, damage):
        self._hp -= damage
        if self._hp <= 0:
            game_objects.remove_slime(self)

    def try_deal_damage(self):
        if self.rect.colliderect(game_objects.player.rect):
            game_objects.remove_slime(self)
            game_objects.player.take_damage(self._damage)
