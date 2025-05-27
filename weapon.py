import math

import pygame.transform
from pygame import SurfaceType

import image_helper
import settings


class Weapon:
    def __init__(self):
        self.angle = 0
        self.weapon_image = image_helper.load_image("images/bow.png", settings.SCALE)
        self.rotated_image = pygame.transform.rotate(self.weapon_image, self.angle)
        self.rect = self.rotated_image.get_rect()

    def update(self, player):
        self.rect.center = player.rect.center
        mouse_pos = pygame.mouse.get_pos()
        x_distance = mouse_pos[0] - self.rect.centerx
        y_distance = -(mouse_pos[1] - self.rect.centery)
        self.angle = math.degrees(math.atan2(y_distance, x_distance))

    def draw(self, surface: SurfaceType):
        self.rotated_image = pygame.transform.rotate(self.weapon_image, self.angle)
        rect = (self.rect.centerx - int(self.rotated_image.get_width() / 2),
                self.rect.centery - int(self.rotated_image.get_height() / 2))
        surface.blit(self.rotated_image, rect)
