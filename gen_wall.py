#!/usr/bin/env python3
from PIL import Image
import sys

dimensions = (1920, 1080)

bg_arg = sys.argv[1]
global bg
if bg_arg[0] == "#":
    bg = Image.new("RGB", dimensions, bg_arg)
else:
    bg = Image.open(bg_arg)

logo = Image.open(sys.argv[2])
logo_fill, logo_mask = logo, logo
if len(sys.argv) > 3:
    logo_fill = Image.new("RGB", logo.size, sys.argv[3])
    logo_fill.paste(logo_fill, (0, 0), logo.convert("L"))

bg.paste(logo_fill, (int(bg.size[0]/2 - logo.size[0]/2), int(bg.size[1]/2 - logo.size[1]/2)), logo_mask)

bg.save("out.png")
