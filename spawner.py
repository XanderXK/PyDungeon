import math
import random
import pygame.time
import game_objects
import potion
import settings
import slime


class Spawner:
    slime_cooldown = 500
    slime_min_cooldown = 75
    slime_spawn_multiplier = 0.99
    potion_cooldown = 5000
    last_potion_spawn_time = 0
    last_slime_spawn_time = 0

    def __init__(self):
        game_objects.objects_to_update.append(self)
        self.last_potion_spawn_time -= self.potion_cooldown
        self.last_slime_spawn_time -= self.slime_cooldown

    def update(self):
        if pygame.time.get_ticks() > self.last_potion_spawn_time + self.potion_cooldown:
            self.spawn_potion()
        if pygame.time.get_ticks() > self.last_slime_spawn_time + self.slime_cooldown:
            self.spawn_slime()

    def spawn_potion(self):
        spawn_pos = (random.randint(100, settings.SCREEN_WIDTH - 100),
                     random.randint(100, settings.SCREEN_HEIGHT - 100))
        potion.Potion(spawn_pos)
        self.last_potion_spawn_time = pygame.time.get_ticks()

    def spawn_slime(self):
        angle = random.randint(1, 360)
        x = (settings.SCREEN_WIDTH / 2) + (math.cos(math.radians(angle)) * settings.SCREEN_WIDTH * 0.7)
        y = (settings.SCREEN_HEIGHT / 2) + (-math.sin(math.radians(angle)) * settings.SCREEN_WIDTH * 0.7)
        slime.Slime((x, y))
        self.last_slime_spawn_time = pygame.time.get_ticks()
        self.slime_cooldown *= self.slime_spawn_multiplier
        if self.slime_cooldown < self.slime_min_cooldown:
            self.slime_cooldown = self.slime_min_cooldown
