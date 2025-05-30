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
    move_speed = 5
    hp =5

    def __init__(self, start_position):
        game_objects.objects_to_update.append(self)
        game_objects.objects_to_draw.append(self)
        self.rect = pygame.Rect(0, 0, 50, 50)
        self.rect.center = start_position
        self.idle_animation = animation_creator.create_player_idle()
        self.run_animation = animation_creator.create_player_run()
        self.current_anim_frame = self.idle_animation.get_frame()
        self.hp_text = screen_text.ScreenText(f"hp: {self.hp}", (50, settings.SCREEN_HEIGHT-35))
        Weapon(self)

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

        self.rect.x += move_x * self.move_speed
        self.rect.y += move_y * self.move_speed

    def draw(self, screen: SurfaceType):
        player_image = pygame.transform.flip(self.current_anim_frame, self._is_flipped, False)
        screen.blit(player_image, self.rect)
        # pygame.draw.rect(screen, (255, 255, 255), self.rect, 1)
