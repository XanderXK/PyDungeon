import pygame
import image_helper
import settings
from animation import Animation


def create_player_idle():
    player_idle_frames = []
    img = pygame.image.load(f"images/player/player.png").convert_alpha()
    img = image_helper.scale_image(img, settings.SCALE)
    player_idle_frames.append(img)
    return Animation(player_idle_frames, 100)

def create_player_run():
    player_run_frames = []
    for item in range(4):
        img = pygame.image.load(f"images/player/player_{item}.png").convert_alpha()
        img = image_helper.scale_image(img, settings.SCALE)
        player_run_frames.append(img)
    return Animation(player_run_frames, 90)