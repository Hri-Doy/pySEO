from PIL import Image, ImageFont, ImageDraw
import random
import textwrap


color_R = random.randint(250,256)
color_G = random.randint(0,256)
color_B = random.randint(0,256)
solidBG = Image.new("RGB", (1200,630), (color_R, color_G, color_B))
W,H = solidBG.size

text = ('How to make a cup of tea').title()

font_path = r'H:\PYTHON SEO\Image Manupulation\Text Image\GingerBrand.ttf'
font = ImageFont.truetype(font_path, 80)

draw = ImageDraw.Draw(solidBG)
draw.text((W/2,H/2), text, font=font, fill='Black', anchor="mm")
solidBG.show()