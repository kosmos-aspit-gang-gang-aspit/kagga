import pygame
class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, images_to_load):
        super().__init__()
        self.index = 0
        self.rect = self.image.get_rect()
        self.animation_speed = 0.2
        self.images = []

        for image in images_to_load:
            image = pygame.image.load(image)
            self.images.append(image)

        self.image = self.images[self.index]


    def update(self):
        self.index += self.animation_speed
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[int(self.index)]
