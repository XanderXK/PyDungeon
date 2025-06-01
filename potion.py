from pygame import SurfaceType
import game_objects
import image_helper
import settings


class Potion:
    def __init__(self, position):
        game_objects.objects_to_draw.append(self)
        game_objects.objects_to_update.append(self)
        self.image = image_helper.load_image("images/potion.png",settings.SCALE)
        self.rect = self.image.get_rect()
        self.rect.center = position

    def update(self):
        if self.rect.colliderect(game_objects.player.rect):
            game_objects.player.add_hp(1)
            game_objects.objects_to_draw.remove(self)
            game_objects.objects_to_update.remove(self)

    def draw(self, screen: SurfaceType):
        screen.blit(self.image, self.rect)