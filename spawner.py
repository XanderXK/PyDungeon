import random

import pygame.time

import game_objects
import potion
import settings
import slime


class Spawner:
    last_potion_spawn_time = 0
    last_slime_spawn_time = 0

    def __init__(self, slime_cooldown, potion_cooldown):
        game_objects.objects_to_update.append(self)
        self.slime_cooldown = slime_cooldown
        self.potion_cooldown = potion_cooldown
        self.last_potion_spawn_time -= potion_cooldown
        self.last_slime_spawn_time -= slime_cooldown

    def update(self):
        if pygame.time.get_ticks() > self.last_potion_spawn_time + self.potion_cooldown:
            self.spawn_potion()
        if pygame.time.get_ticks() > self.last_slime_spawn_time + self.last_slime_spawn_time:
            self.spawn_slime()

    def spawn_potion(self):
        spawn_pos = (random.randint(100, settings.SCREEN_WIDTH - 100),
                     random.randint(100, settings.SCREEN_HEIGHT - 100))
        potion.Potion(spawn_pos)
        self.last_potion_spawn_time = pygame.time.get_ticks()

    def spawn_slime(self):
        spawn_pos = (random.randint(100, settings.SCREEN_WIDTH - 100),
                     random.randint(100, settings.SCREEN_HEIGHT - 100))
        slime.Slime(spawn_pos)
        self.last_slime_spawn_time = pygame.time.get_ticks()
