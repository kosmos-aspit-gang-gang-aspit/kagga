from PIL import Image
import json

# block = FFAA00
# Mario = FF0000

map_image = Image.open("map_image.png")
w, h = map_image.size

for row in range(h):
    for column in range(w):
        pixel = map_image.getpixel((row, column))
        if pixel == (0, 0, 0):
            continue
        elif pixel == (255, 170, 0):
            continue
            # TODO: create block in dict and save as json