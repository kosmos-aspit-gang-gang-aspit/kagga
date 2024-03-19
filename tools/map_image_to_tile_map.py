from PIL import Image
import json
import os

# block = FFAA00
# Mario = FF0000

map_image = Image.open("../map_image.png")
map_image = map_image.convert("RGB")
w, h = map_image.size

map_export = {
    "map": []
}

for row in range(w):
    for column in range(h):
        pixel = map_image.getpixel((row, column))
        tile = {}
        if pixel == (0, 0, 0):
            continue
        elif pixel == (255, 170, 0):
            tile["type"] = "block"
        elif pixel == (255, 0, 0):
            tile["type"] = "mario_spawn"


        tile["pos"] = [row * 50, column * 50]
        map_export["map"].append(tile)

os.remove("tilemap.json")
with open("tilemap.json", "w") as f:
    json.dump(map_export, f)