import os
import pygame
import keyboard
from animation import AnimatedSprite


class Mario(AnimatedSprite):
    def __init__(self):
        # load mario sprites
        _dir = "sprites/mario"
        for filename in os.listdir(_dir):
            filepath = os.path.join(_dir, filename)
            pygame.image.load(filepath)

        # init animation
        super().__init__()

        self.speed = 2

    def move_up(self):
        self.rect.y -= self.speed

    def move_left(self):
        self.rect.x -= self.speed

    def move_down(self):
        self.rect.y += self.speed

    def move_right(self):
        self.rect.x += self.speed

    def use(self):
        print("Space was pressed")


class Game:
    def __init__(self):
        self.screen_width = pygame.display.Info().current_w
        self.screen_height = pygame.display.Info().current_h
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        self.mario = Mario()

    def game(self):
        pygame.init()

        pygame.time.Clock().tick(12)  # FPS cap

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if keyboard.is_pressed('w'):
                self.mario.move_up()
            if keyboard.is_pressed('a'):
                self.mario.move_left()
            if keyboard.is_pressed('s'):
                self.mario.move_down()
            if keyboard.is_pressed('d'):
                self.mario.move_right()

            self.mario.update()

        pygame.quit()  # safely close pygame, i think.

