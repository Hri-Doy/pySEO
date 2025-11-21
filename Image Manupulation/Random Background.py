from PIL import Image
import random
'''
# New Image = Image.new
# Mode : RGB
# Size : 1200,630
# Color : white(255, 255, 255)
# '''
img = Image.new("RGB",(1200,630),(255, 255, 255))
# img.show()


"""
# Images with Random Color
# import random
# Random number limit : random.randint(0,255)

"""
num1 = random.randint(0,255)
num2 = random.randint(0,255)
num3 = random.randint(0,255)
imge = Image.new("RGB", (1200,630),(num1,num2,num3))
# img.show()

"""
# Random Color IMG with While Loop
# Let's suppose I want 200 images
# clr = colour
"""
i = 0
while i < 5:
    clr1 = random.randint(0,255)
    clr2 = random.randint(0,255)
    clr3 = random.randint(0,255)
    solid_color = Image.new("RGB",(1200,630),(clr1, clr2, clr3))
    solid_color.save('Image Manupulation/Solid BG/'+str(i)+'.jpg')
    i += 1

