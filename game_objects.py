player = None
slimes = []
objects_to_update = []
objects_to_draw = []

_projectiles = []


def add_slime(slime):
    slimes.append(slime)
    objects_to_update.append(slime)
    objects_to_draw.append(slime)


def remove_slime(slime):
    slimes.remove(slime)
    objects_to_update.remove(slime)
    objects_to_draw.remove(slime)


def add_projectile(projectile):
    _projectiles.append(projectile)
    objects_to_update.append(projectile)
    objects_to_draw.append(projectile)


def remove_projectile(projectile):
    _projectiles.remove(projectile)
    objects_to_update.remove(projectile)
    objects_to_draw.remove(projectile)
