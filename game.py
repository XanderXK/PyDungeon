import game_objects
import settings
from screen_text import ScreenText


def finish():
    game_objects.objects_to_update.clear()
    game_objects.objects_to_draw.clear()
    ScreenText("You are good!", (settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2))
