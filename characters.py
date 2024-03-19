from animation import AnimatedSprite
import os
import pygame
class Mario(AnimatedSprite):
    def __init__(self, screen, spawnpoint):
        # load mario sprites
        idle_sprites = []
        walking_sprites = []
        jumping_sprites = []
        _dir = "sprites/mario/idle_sprites"
        for filename in os.listdir(_dir):
            filepath = os.path.join(_dir, filename)
            sprite = pygame.image.load(filepath).convert_alpha()  # alpha conversion optimizes performance
            idle_sprites.append(sprite)
        _dir = "sprites/mario/walking_sprites"
        for filename in os.listdir(_dir):
            filepath = os.path.join(_dir, filename)
            sprite = pygame.image.load(filepath).convert_alpha()  # alpha conversion optimizes performance
            walking_sprites.append(sprite)
        _dir = "sprites/mario/jumping_sprites"
        for filename in os.listdir(_dir):
            filepath = os.path.join(_dir, filename)
            sprite = pygame.image.load(filepath).convert_alpha()  # alpha conversion optimizes performance
            jumping_sprites.append(sprite)

        # init animation
        super().__init__(idle_sprites=idle_sprites, walking_sprites=walking_sprites, jumping_sprites=jumping_sprites, screen=screen)

        self.rect.x = spawnpoint[0]
        self.rect.y = spawnpoint[1]
        # player movement
        self.speed = 10
        self.jump_power = self.speed * 3
        self.vx = 0  # velocity x-axis
        self.vy = 0  # velocity y-axis

        # player state
        self.moving = False
        self.flipped = False
        self.airborne = False
        self.crouched = False

    def move_up(self):
        self.vy -= self.jump_power
        self.airborne = True  # this needs to be reset somewhere

    def move_left(self):
        self.vx -= self.speed
        self.flipped = True

    def move_down(self):
        self.crouched = True
        # couch

    def move_right(self):
        self.vx += self.speed
        self.flipped = False