#!/usr/bin/env python3
from PIL import Image
import sys

dimensions = (600, 600)

bg = Image.new("RGBA", dimensions, "#00000000")

logo = Image.open("logos/star-antlers.png")
logo = logo.convert("L")
logo_fill = Image.new("RGBA", logo.size, "#ffffff")

bg.paste(logo_fill, (0, 0), logo)

bg.save("transformed.png")
