from PIL import Image

logo = Image.open("star-and-antlers.png")
logo = logo.convert("L")

bg = Image.open("bg.png")
bg.paste(logo, (int(bg.size[0]/2 - logo.size[0]/2), int(bg.size[1]/2 - logo.size[1]/2)), logo)

bg.save("out.png")
