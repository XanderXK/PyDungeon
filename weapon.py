import math
import game_objects
import image_helper
import settings
import pygame.transform
from pygame import SurfaceType
from projectile import Projectile


class Weapon:
    cooldown = 125
    last_cooldown_time = pygame.time.get_ticks()

    def __init__(self, player):
        game_objects.objects_to_update.append(self)
        game_objects.objects_to_draw.append(self)
        self.player = player
        self.angle = 0
        self.weapon_image = image_helper.load_image("images/bow.png", settings.SCALE)
        self.rotated_image = pygame.transform.rotate(self.weapon_image, self.angle)
        self.rect = self.rotated_image.get_rect()

    def update(self):
        self.calculate_angle()
        if pygame.mouse.get_pressed()[0] and pygame.time.get_ticks() - self.last_cooldown_time > self.cooldown:
            self.shoot()

    def calculate_angle(self):
        self.rect.center = self.player.rect.center
        mouse_pos = pygame.mouse.get_pos()
        x_distance = mouse_pos[0] - self.rect.centerx
        y_distance = -(mouse_pos[1] - self.rect.centery)
        self.angle = math.degrees(math.atan2(y_distance, x_distance))

    def shoot(self):
        spawn_pos = self.get_projectile_spawn_pos()
        Projectile(spawn_pos[0], spawn_pos[1], self.angle)
        self.last_cooldown_time = pygame.time.get_ticks()

    def get_projectile_spawn_pos(self):
        x = self.rect.centerx + math.cos(math.radians(self.angle)) * 50
        y = self.rect.centery + math.sin(math.radians(self.angle)) * -50
        return x, y

    def draw(self, screen: SurfaceType):
        self.rotated_image = pygame.transform.rotate(self.weapon_image, self.angle)
        rect = (self.rect.centerx - int(self.rotated_image.get_width() / 2),
                self.rect.centery - int(self.rotated_image.get_height() / 2))
        screen.blit(self.rotated_image, rect)
