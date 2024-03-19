import pygame


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, images, screen):
        super().__init__()
        self.index = 0
        self.animation_speed = 0.2
        self.images = images
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.screen = screen

    def update(self):
        self.index += self.animation_speed
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[int(self.index)]
        # drawing moved here:
        self.screen.fill((0, 0, 0))  # clear the screen with black, placeholder for background
        self.screen.blit(self.image, self.rect)  # draw the sprite
        pygame.display.flip()  # update the screen
        # not entirely sure why this works just tried things
