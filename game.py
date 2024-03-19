import os
import pygame
from animation import AnimatedSprite


class Mario(AnimatedSprite):
    def __init__(self, screen):
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

    def move_up(self):
        self.rect.y -= self.speed

    def move_left(self):
        self.rect.x -= self.speed

    def move_down(self):
        self.rect.y += self.speed

    def move_right(self):
        self.rect.x += self.speed


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
            if keys[pygame.K_w]:
                self.mario.move_up()
            if keys[pygame.K_a]:
                self.mario.move_left()
                self.mario.moving = True
                self.mario.flipped = True
            if keys[pygame.K_s]:
                self.mario.move_down()
                self.mario.crouched = True
            if keys[pygame.K_d]:
                self.mario.move_right()
                self.mario.moving = True
                self.mario.flipped = False

            self.mario.update()
            self.mario.moving = False
            self.mario.crouched = False
            clock.tick(24)  # FPS cap

        pygame.quit()  # safely close pygame, i think.
