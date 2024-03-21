import pygame
import json
import characters as char
import constants

with open("map.json", "r") as f:
    map_dict = json.load(f)["map"]

mario = None
screen = None
mario_spawn = []

def get_map(_screen=None):
    global mario
    global mario_spawn
    global screen
    screen_not_loaded = True if _screen is None or screen is None else False

    game_map_sprites = pygame.sprite.Group()
    for gameobj in map_dict:
        if gameobj["type"] == "block":
            block_sprite = pygame.sprite.Sprite()  # Create sprite instance

            block_sprite = pygame.sprite.Sprite()  # Create sprite instance
            block_image = pygame.image.load("sprites/environment/block.png")
            block_image = pygame.transform.scale(block_image, (int(50 * constants.scalar), int(50 * constants.scalar)))  # Scale image correctly
            block_sprite.image = block_image
            block_sprite.rect = block_sprite.image.get_rect()
            block_sprite.rect.x = int(gameobj["pos"][0] * constants.scalar)
            block_sprite.rect.y = int(gameobj["pos"][1] * constants.scalar)

            game_map_sprites.add(block_sprite)  # Add the sprite to the group

        if gameobj["type"] == "mario_spawn":
            mario_spawn = [gameobj["pos"][0] * constants.scalar, gameobj["pos"][1] * constants.scalar]
            if screen_not_loaded:
                print("Screen not passed or loaded, waiting with giving the game Mario.")
            else:
                mario = char.Mario(_screen if screen is None else screen, mario_spawn)

    return game_map_sprites

def get_mario():
    global mario
    if mario is None:
        mario = char.Mario(screen, mario_spawn)
    return mario

def load_screen(_screen):
    global screen
    screen = _screen
