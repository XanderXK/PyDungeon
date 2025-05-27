import math
import pygame
from pygame import SurfaceType
import animation
import animation_creator
import settings


class Player:
    is_flipped = False
    anim_cooldown = 90

    def __init__(self, start_position):
        self.rect = pygame.Rect(0, 0, 50, 50)
        self.rect.center = start_position
        self.idle_animation = animation_creator.create_player_idle()
        self.run_animation = animation_creator.create_player_run()
        self.current_anim_frame = self.idle_animation.get_frame()

    def draw(self, surface: SurfaceType):
        player_image = pygame.transform.flip(self.current_anim_frame, self.is_flipped, False)
        surface.blit(player_image, self.rect)
        pygame.draw.rect(surface, (255, 255, 255), self.rect, 1)

    def move(self, input_x: int, input_y: int):
        if input_x != 0 and input_y != 0:
            input_x = input_x * (math.sqrt(2) / 2)
            input_y = input_y * (math.sqrt(2) / 2)

        if input_x + input_y > 0:
            self.current_anim_frame = self.run_animation.get_frame()
        else:
            self.current_anim_frame = self.idle_animation.get_frame()

        if input_x > 0:
            self.is_flipped = False
        elif input_x < 0:
            self.is_flipped = True

        self.rect.x += input_x * settings.PLAYER_SPEED
        self.rect.y += input_y * settings.PLAYER_SPEED
