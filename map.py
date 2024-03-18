import pygame
import json

with open("map.json", "r") as f:
    map_dict = json.load(f)["map"]

def get_map():
    game_map_sprites = []
    for gameobj in map_dict:
        gameobj_export = pygame.sprite.Sprite()
        if gameobj["type"] == "block":
            gameobj_export.image = pygame.image.load("sprites/environment/block.png")
            gameobj_export.rect = gameobj_export.image.get_rect()

        gameobj_export.rect.x = gameobj["pos"][0]
        gameobj_export.rect.y = gameobj["pos"][1]

        game_map_sprites.append(gameobj_export)

    return game_map_sprites