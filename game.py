import pygame
import keyboard
import time

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

class Mario(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/image_7.png")
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

    def move_up(self):
        self.rect.y -= 10

    def move_left(self):
        self.rect.x -= 10

    def move_down(self):
        self.rect.y += 10

    def move_right(self):
        self.rect.x += 10

    def use(self):
        print("Space was pressed")


mario = Mario()

all_sprites = pygame.sprite.Group()
all_sprites.add(mario)

"""
keyboard.add_hotkey('w', lambda: mario.move_up())
keyboard.add_hotkey('a', lambda: mario.move_left())
keyboard.add_hotkey('s', lambda: mario.move_down())
keyboard.add_hotkey('d', lambda: mario.move_right())
keyboard.add_hotkey('space', lambda: mario.use())"""


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if keyboard.is_pressed('w'):
        mario.move_up()
    if keyboard.is_pressed('a'):
        mario.move_left()
    if keyboard.is_pressed('s'):
        mario.move_down()
    if keyboard.is_pressed('d'):
        mario.move_right()

    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()

