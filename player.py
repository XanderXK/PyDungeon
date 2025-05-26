import math
import pygame
from pygame import SurfaceType

import settings


class Player:
    is_flipped = False
    anim_cooldown = 90

    def __init__(self, x, y, player_anim):
        self.rect = pygame.Rect(0, 0, 50, 50)
        self.rect.center = (x, y)
        self.player_anim = player_anim
        self.update_time = pygame.time.get_ticks()
        self.current_frame = 0
        self.image = player_anim[self.current_frame]

    def draw(self, surface: SurfaceType):
        if pygame.time.get_ticks() - self.update_time > self.anim_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.current_frame += 1
            if self.current_frame >= len(self.player_anim):
                self.current_frame = 0
            self.image = self.player_anim[self.current_frame]

        player_image = pygame.transform.flip(self.image, self.is_flipped, False)
        surface.blit(player_image, self.rect)
        pygame.draw.rect(surface, (255, 255, 255), self.rect, 1)

    def move(self, input_x: int, input_y: int):
        if input_x != 0 and input_y != 0:
            input_x = input_x * (math.sqrt(2) / 2)
            input_y = input_y * (math.sqrt(2) / 2)

        if input_x > 0:
            self.is_flipped = False
        elif input_x < 0:
            self.is_flipped = True

        self.rect.x += input_x * settings.PLAYER_SPEED
        self.rect.y += input_y * settings.PLAYER_SPEED
