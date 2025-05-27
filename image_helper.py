import pygame.surface


def load_image(path: str, scale: float):
    img = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(img, (img.get_width() * scale, img.get_height() * scale))
