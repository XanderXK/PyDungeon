import pygame
import animation_creator
import settings
from player import Player

pygame.init()
pygame.display.set_caption("PyDungeon")

screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
clock = pygame.time.Clock()

player = Player(settings.PLAYER_START_POSITION)

input_x = 0
input_y = 0

run = True
while run:
    screen.fill(settings.BACKGROUND)
    clock.tick(settings.FPS)

    player.move(input_x, input_y)
    player.draw(screen)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                input_y = -1
            if event.key == pygame.K_s:
                input_y = 1
            if event.key == pygame.K_a:
                input_x = -1
            if event.key == pygame.K_d:
                input_x = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w and input_y == -1:
                input_y = 0
            if event.key == pygame.K_s and input_y == 1:
                input_y = 0
            if event.key == pygame.K_a and input_x == -1:
                input_x = 0
            if event.key == pygame.K_d and input_x == 1:
                input_x = 0

        if event.type == pygame.QUIT:
            run = False

pygame.quit()
