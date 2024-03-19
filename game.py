import os
import pygame
from animation import AnimatedSprite


class Mario(AnimatedSprite):
    def __init__(self, screen):
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


class Game:
    def __init__(self):
        pygame.init()
        self.screen_width = pygame.display.Info().current_w
        self.screen_height = pygame.display.Info().current_h
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        self.mario = Mario(self.screen)

    def game(self):
        clock = pygame.time.Clock()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()  # pygame has a built in keyboard function with better performance
            if keys[pygame.K_w] and not self.mario.airborne:
                self.mario.move_up()
            if keys[pygame.K_a]:
                self.mario.move_left()
            if keys[pygame.K_s]:
                self.mario.move_down()
            if keys[pygame.K_d]:
                self.mario.move_right()

            if not (keys[pygame.K_a] or keys[pygame.K_d]):
                self.mario.moving = False
            else:
                self.mario.moving = True

            self.mario.update(flipped=self.mario.flipped)
            self.mario.crouched = False
            clock.tick(24)  # FPS cap

        pygame.quit()  # safely close pygame, i think.
