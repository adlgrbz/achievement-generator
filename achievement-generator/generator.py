from os import getcwd
from PIL import Image, ImageDraw, ImageFont

#for background image
HEIGHT = 64
WIDTH = 320

ITEM_SIZE = 32

FONT = "./others/minecraft-font.ttf"
FONT_SIZE = 16
COLORS = [(255, 255, 0), (255, 255, 255)]

def make(contents, item_name, file_name):

    bg_img = Image.open("./others/background")
    item = Image.open("./items/"+item_name)

    bg_img.paste(item, (16, 16), mask=item)

    draw = ImageDraw.Draw(bg_img)
    font = ImageFont.truetype(FONT, FONT_SIZE)

    #align posts
    val0 = [HEIGHT / 4, (HEIGHT / 2) + (ITEM_SIZE / 4)]
    val1 = FONT_SIZE / 2

    #+3 = backround image border height size
    for i in range(2):
        draw.text((FONT_SIZE+ITEM_SIZE+8, (val0[i] - val1)+3),
                  contents[i], COLORS[i], font=font)

    bg_img.save(getcwd()+"/"+file_name)
