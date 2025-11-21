from PIL import Image

# img = Image.open('Image Manupulation/picture.jpg')
# left, upper, right, lower
# x, y, x + w, y + h
# cropper = img.crop((300, 200, 600, 500))
# cropper.show()


'''The Following Code
Removes the border from the image.
'''
b_img = Image.open('Image Manupulation/Borderd Image.png')
width, height = b_img.size
img_new = b_img.crop((130, 40, width-130, height-40))
img_new.save('Image Manupulation/Removed Border.png')
img_new.show()