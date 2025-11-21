from PIL import Image
file = r'Image Manupulation/picture.jpg'
img = Image.open(file)
img.show()
img.save('WP/nature.jpg')