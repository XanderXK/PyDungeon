import math
import pygame
from pygame import SurfaceType
import animation_creator
import game_objects
import player_input
import settings
from weapon import Weapon


class Player:
    is_flipped = False
    anim_cooldown = 90

    def __init__(self, start_position):
        game_objects.objects_to_update.append(self)
        game_objects.objects_to_draw.append(self)
        self.rect = pygame.Rect(0, 0, 50, 50)
        self.rect.center = start_position
        self.idle_animation = animation_creator.create_player_idle()
        self.run_animation = animation_creator.create_player_run()
        self.current_anim_frame = self.idle_animation.get_frame()
        Weapon(self)

    def draw(self, surface: SurfaceType):
        player_image = pygame.transform.flip(self.current_anim_frame, self.is_flipped, False)
        surface.blit(player_image, self.rect)
        pygame.draw.rect(surface, (255, 255, 255), self.rect, 1)

    def update(self):
        move_x = player_input.x
        move_y = player_input.y
        if move_x != 0 and move_y != 0:
            move_x = move_x * (math.sqrt(2) / 2)
            move_y = move_y * (math.sqrt(2) / 2)

        if move_y + move_x == 0:
            self.current_anim_frame = self.idle_animation.get_frame()
        else:
            self.current_anim_frame = self.run_animation.get_frame()

        if move_x > 0:
            self.is_flipped = False
        elif move_x < 0:
            self.is_flipped = True

        self.rect.x += move_x * settings.PLAYER_SPEED
        self.rect.y += move_y * settings.PLAYER_SPEED
