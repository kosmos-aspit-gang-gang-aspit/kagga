import pygame
import constants

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, idle_sprites, walking_sprites, jumping_sprites, screen):
        super().__init__()
        self.index = 0
        self.animation_speed = 0.2
        self.images = walking_sprites
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.vx = 0
        self.vy = 0
        self.screen = screen

        # create hitbox
        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)

    def update(self, flipped, ground_hitboxes):
        # index sprites
        self.index += self.animation_speed
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[int(self.index)]

        # update
        self.image = pygame.transform.flip(self.images[int(self.index)], flipped, False)

        friction_coefficient = 0.7  # velocity factor
        gravity = 3  # gravity factor
        gravity_scale = 1.15  # gravity time scale

        self.vx *= friction_coefficient
        self.vy *= friction_coefficient

        self.vy += gravity  # apply gravity
        self.vy *= gravity_scale  # increase speed of gravity over time.

        self.rect.x += self.vx
        self.rect.y += self.vy

        self.hitbox.center = self.rect.center  # re-center hitbox

        # check for collision here:
        ground_collisions = pygame.sprite.spritecollide(self, ground_hitboxes, dokill=False)  #self.hitbox??
        for ground_hitbox in ground_collisions:
            if self.vy > 0:
                self.vy = 0
                self.rect.bottom = ground_hitbox.top

        # draw
        self.screen.fill((0, 0, 0))  # clear the screen with black, placeholder for background
        self.image = pygame.transform.scale_by(self.image, constants.scalar)
        self.screen.blit(self.image, self.rect)  # draw the sprite
        pygame.display.flip()  # update the screen
