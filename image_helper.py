import pygame.surface


def scale_image(image: pygame.surface.Surface, scale: float):
    return pygame.transform.scale(image, (image.get_width() * scale, image.get_height() * scale))
