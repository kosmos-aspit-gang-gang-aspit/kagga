from animation import AnimatedSprite
import os
import pygame
class Mario(AnimatedSprite):
    def __init__(self, screen, spawnpoint):
        # load mario sprites
        sprites = []
        _dir = "sprites/mario"
        for filename in os.listdir(_dir):
            filepath = os.path.join(_dir, filename)
            sprite = pygame.image.load(filepath).convert_alpha()  # alpha conversion optimizes performance
            sprites.append(sprite)

        # init animation
        super().__init__(sprites, screen)

        self.speed = 10
        self.moving = False
        self.flipped = False
        self.airborne = False
        self.crouched = False
        self.rect.x = spawnpoint[0]
        self.rect.y = spawnpoint[1]

    def move_up(self):
        self.rect.y -= self.speed

    def move_left(self):
        self.rect.x -= self.speed

    def move_down(self):
        self.rect.y += self.speed

    def move_right(self):
        self.rect.x += self.speed