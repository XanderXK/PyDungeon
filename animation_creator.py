import image_helper
import settings
from animation import Animation


def create_player_idle():
    player_idle_frames = []
    img = image_helper.load_image(f"images/player.png", settings.SCALE)
    player_idle_frames.append(img)
    return Animation(player_idle_frames, 100)


def create_player_run():
    player_run_frames = []
    for item in range(4):
        img = image_helper.load_image(f"images/player_{item}.png", settings.SCALE)
        player_run_frames.append(img)
    return Animation(player_run_frames, 90)
