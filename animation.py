import pygame.time


class Animation:
    current_frame_index=0

    def __init__(self, anim_frames, cooldown: float):
        self.anim_frames = anim_frames
        self.cooldown = cooldown
        self.last_update_time = pygame.time.get_ticks()

    def get_frame(self):
        if pygame.time.get_ticks() - self.last_update_time > self.cooldown:
            self.last_update_time = pygame.time.get_ticks()
            self.current_frame_index += 1
            if self.current_frame_index >= len(self.anim_frames):
                self.current_frame_index = 0
        return self.anim_frames[self.current_frame_index]


