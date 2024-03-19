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

    game_map_sprites = []
    for gameobj in map_dict:
        gameobj_export = pygame.sprite.Sprite()
        if gameobj["type"] == "block":
            gameobj_export.image = pygame.image.load("sprites/environment/block.png")
            gameobj_export.image = pygame.transform.scale_by(gameobj_export.image, constants.scalar)
            gameobj_export.rect = gameobj_export.image.get_rect()
            gameobj_export.rect.width = int(50 * constants.scalar)
            gameobj_export.rect.height = int(50 * constants.scalar)


            gameobj_export.rect.x = int(gameobj["pos"][0] * constants.scalar)
            gameobj_export.rect.y = int(gameobj["pos"][1] * constants.scalar)

            game_map_sprites.append(gameobj_export)
        if gameobj["type"] == "mario_spawn":
            mario_spawn = [gameobj["pos"][0] * constants.scalar, gameobj["pos"][1] * constants.scalar]
            if screen_not_loaded:
                print("Screen not passed or loaded, waiting with giving the game Mario.")
            else:
                mario = char.Mario(_screen if screen is None else screen, mario_spawn)



        # gameobj_export.rect.x = gameobj["pos"][0]
        # gameobj_export.rect.y = gameobj["pos"][1]
        #
        # game_map_sprites.append(gameobj_export)

    return game_map_sprites

def get_mario():
    global mario
    if mario is None:
        mario = char.Mario(screen, mario_spawn)
    return mario

def load_screen(_screen):
    global screen
    screen = _screen