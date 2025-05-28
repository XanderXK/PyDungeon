import math

import pygame.sprite

import image_helper
import settings


class Projectile(pygame.sprite.Sprite):
    speed = 5

    def __init__(self, x, y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = image_helper.load_image("images/arrow.png", settings.SCALE)
        self.angle = angle
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.dx = math.cos(math.radians(angle)) * self.speed
        self.dy = -math.sin(math.radians(angle)) * self.speed

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

    def draw(self, surface):
        rect = (self.rect.centerx - int(self.image.get_width() / 2),
                self.rect.centery - int(self.image.get_height() / 2))
        surface.blit(self.image, rect)
        # self.projectile_group.draw(surface)
