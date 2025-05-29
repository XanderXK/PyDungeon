import pygame
import game_objects
import player_input
import screen_text
import settings
from player import Player
from slime import Slime
from weapon import Weapon

pygame.init()
pygame.display.set_caption("PyDungeon")

surface = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
clock = pygame.time.Clock()

player = Player(settings.PLAYER_START_POSITION)

for i in range(5):
    slime = Slime((500 + i * 100, 300 + i * 50))

text = screen_text.ScreenText("PyDungeon", (100, 35))

run = True
while run:
    surface.fill(settings.BACKGROUND)
    clock.tick(settings.FPS)

    for object_to_update in game_objects.objects_to_update:
        object_to_update.update()

    for object_to_draw in game_objects.objects_to_draw:
        object_to_draw.draw(surface)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_input.y = -1
            if event.key == pygame.K_s:
                player_input.y = 1
            if event.key == pygame.K_a:
                player_input.x = -1
            if event.key == pygame.K_d:
                player_input.x = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w and player_input.y == -1:
                player_input.y = 0
            if event.key == pygame.K_s and player_input.y == 1:
                player_input.y = 0
            if event.key == pygame.K_a and player_input.x == -1:
                player_input.x = 0
            if event.key == pygame.K_d and player_input.x == 1:
                player_input.x = 0

        if event.type == pygame.QUIT:
            run = False

pygame.quit()
