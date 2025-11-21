from PIL import Image

img1 = Image.open('Image Manupulation/Image Pasting/1.png')
img2 = Image.open('Image Manupulation/Image Pasting/2.png')

"""
# Image Mode : RGB
# Image Size : 1200, 630
# Image Color in RGB : 255,255,255
# """

solid_clr = Image.new("RGB", (1980,1140),(255,255,255))
solid_clr.paste(img2,(30,30))
#solid_clr.show()

"""
# Save with compression
neo = solid_clr.save('output.webp', quality=50, optimize=True, progressive=True)
"""


img5 = Image.open('Image Manupulation/Image Pasting/2.png')
bg_solid = Image.new("RGB", (1980,1140), (255,190,90))
# Resize the Image5
w,h = img5.size
# print(w,h)
resized = img5.resize((1970,1120))
# resized.show()
bg_solid.paste(img5,(30,30))
bg_solid.show()