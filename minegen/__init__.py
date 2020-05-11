from argparse import ArgumentParser
from os import listdir, getcwd, path
from PIL import Image, ImageDraw, ImageFont


__version__ = "2.0.0"

this_dir, this_filename = path.split(__file__)

items = []
yellow = (255, 255, 0)
white = (255, 255, 255)

for name in listdir(f"{this_dir}/data/items"):
    items.append(name.split(".")[0])


def generate(texts, item_name, file_name="output.png"):
    bg = Image.open(f"{this_dir}/data/background.png")
    item = Image.open(f"{this_dir}/data/items/{item_name}.png")
    bg.paste(item, (17, 16), mask=item)

    draw = ImageDraw.Draw(bg)
    font = ImageFont.truetype(f"{this_dir}/data/minecraft-font.ttf", 16)

    draw.text((60, 8), texts[0], yellow, font=font)
    draw.text((60, 30), texts[1], white, font=font)

    bg.save(f"{getcwd()}/{file_name}")
    print("Successful!")


def launch():
    parser = ArgumentParser(usage="%(prog)s [options] output.png")
    parser.description = "Minecraft achievement generator"
    parser.epilog = 'Example: %(prog)s -t Diamonds! -b "Acquire diamonds" -i diamond'

    parser.add_argument("-t", help="Top text", dest="top")
    parser.add_argument("-b", help="Bottom text", dest="bottom")
    parser.add_argument("-i", help="Item name", dest="item")
    parser.add_argument(
        "-o", help="Output file (default: output.png)", default="output.png"
    )
    parser.add_argument("-l", help="Return item list", action="store_true")
    parser.add_argument(
        "-v", help="Version info", action="version", version=f"%(prog)s {__version__}",
    )

    args = parser.parse_args()

    if args.l:
        print(f"Item list: {', '.join(items)}")

    if args.top and args.bottom and args.item:
        if not (f"{args.item}.png") in listdir(f"{this_dir}/data/items"):
            parser.error(f"Item name not found!")

        generate([args.top, args.bottom], args.item, args.o)
