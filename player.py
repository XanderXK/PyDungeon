import math
import pygame
import animation_creator
import game_objects
import player_input
import screen_text
import settings
from pygame import SurfaceType
from weapon import Weapon


class Player:
    _is_flipped = False
    _coins = 0
    move_speed = 5
    _hp = 5
    _max_hp=10

    def __init__(self, start_position):
        game_objects.objects_to_update.append(self)
        game_objects.objects_to_draw.append(self)
        game_objects.player = self
        self.rect = pygame.Rect(0, 0, 50, 50)
        self.rect.center = start_position
        self.idle_animation = animation_creator.create_player_idle()
        self.run_animation = animation_creator.create_player_run()
        self.current_anim_frame = self.idle_animation.get_frame()
        self.hp_text = screen_text.ScreenText(f"hp: {self._hp} / {self._max_hp}", (100, settings.SCREEN_HEIGHT - 35))
        self.score_text = screen_text.ScreenText(f"score: {self._coins}", (250, settings.SCREEN_HEIGHT - 35))
        Weapon(self)

    def add_hp(self, amount):
        self._hp += amount
        if self._hp> self._max_hp:
            self._hp = self._max_hp
        self.hp_text.set_text(f"hp: {self._hp} / {self._max_hp}")

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
            self._is_flipped = False
        elif move_x < 0:
            self._is_flipped = True

        end_pos_x = self.rect.x + move_x * self.move_speed
        end_pos_y = self.rect.y + move_y * self.move_speed
        if end_pos_x > settings.SCREEN_WIDTH - 10 or end_pos_x < 10:
            end_pos_x = self.rect.x
        if end_pos_y > settings.SCREEN_HEIGHT - 100 or end_pos_y < 50:
            end_pos_y = self.rect.y

        self.rect.x = end_pos_x
        self.rect.y = end_pos_y

    def draw(self, screen: SurfaceType):
        player_image = pygame.transform.flip(self.current_anim_frame, self._is_flipped, False)
        screen.blit(player_image, self.rect)
        # pygame.draw.rect(screen, (255, 255, 255), self.rect, 1)
