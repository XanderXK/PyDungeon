import math
import pygame.sprite

import game_objects
import image_helper
import settings


class Projectile:
    speed = 5
    damage = 1

    def __init__(self, x, y, angle):
        game_objects.add_projectile(self)
        self.original_image = image_helper.load_image("images/arrow.png", settings.SCALE)
        self.angle = angle
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = pygame.Rect(0, 0, 10, 10)
        self.rect.center = (x, y)
        self.dx = math.cos(math.radians(angle)) * self.speed
        self.dy = -math.sin(math.radians(angle)) * self.speed

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        for slime in game_objects.slimes:
            if slime.rect.colliderect(self.rect):
                slime.take_damage(self.damage)
                game_objects.remove_projectile(self)
                return

        if (self.rect.right < 0
                or self.rect.left > settings.SCREEN_WIDTH
                or self.rect.bottom < 0
                or self.rect.top > settings.SCREEN_HEIGHT):
            game_objects.remove_projectile(self)

    def draw(self, screen):
        rect = (self.rect.centerx - int(self.image.get_width() / 2),
                self.rect.centery - int(self.image.get_height() / 2))
        screen.blit(self.image, rect)
        # pygame.draw.rect(screen, (0, 0, 255), self.rect, 1)
