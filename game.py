import pygame
import map as tilemap

_map = tilemap.get_map()
map_group = pygame.sprite.Group()
map_group.add(_map)
print(_map)

class Game:
    def __init__(self):
        pygame.init()
        self.screen_width = pygame.display.Info().current_w
        self.screen_height = pygame.display.Info().current_h
        self.screen = pygame.display.set_mode((480, 320))
        tilemap.load_screen(self.screen)
        self.mario = tilemap.get_mario()

    def game(self):
        clock = pygame.time.Clock()

        camera_offset = [self.mario.rect.x, self.mario.rect.y]
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

            self.mario.update(flipped=self.mario.flipped, ground_hitboxes=_map)
            self.mario.crouched = False
            map_group.update()
            map_group.draw(self.screen)
            pygame.display.update()
            clock.tick(24)  # FPS cap

        pygame.quit()  # safely close pygame, i think.
