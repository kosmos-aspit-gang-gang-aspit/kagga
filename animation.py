import pygame
class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, images):
        super().__init__()
        self.index = 0
        self.animation_speed = 0.2
        self.images = images
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100


    def update(self):
        self.index += self.animation_speed
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[int(self.index)]


