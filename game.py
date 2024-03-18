import pygame
import keyboard


class Mario(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/image_7.png")
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
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


def game():
    pygame.init()

    screen_width = pygame.display.Info().current_w
    screen_height = pygame.display.Info().current_h

    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

    mario = Mario()

    pygame.time.Clock().tick(12)  # FPS cap

    all_sprites = pygame.sprite.Group()
    all_sprites.add(mario)

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

