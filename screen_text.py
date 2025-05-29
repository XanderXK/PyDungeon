import pygame.sysfont
import game_objects
from pygame import SurfaceType


class ScreenText:
    def __init__(self, text, position):
        game_objects.objects_to_draw.append(self)
        font = pygame.sysfont.SysFont("Arial", 32)
        self.text_surface = font.render(text, True, (255, 255, 255), (0, 0, 0))
        self.rect = self.text_surface.get_rect()
        self.rect.center = position

    def draw(self, screen: SurfaceType):
        screen.blit(self.text_surface, self.rect)
