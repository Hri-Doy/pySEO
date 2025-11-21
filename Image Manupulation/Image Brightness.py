from PIL import Image, ImageEnhance

img = Image.open('Image Manupulation/picture.jpg')

# Create an Enhancer
color_enhancer = ImageEnhance.Color(img) #Vibrance
contrast_enhancer = ImageEnhance.Contrast(img) #Contrast
brightness_enhancer = ImageEnhance.Brightness(img) #Contrast
sharpness_enhancer = ImageEnhance.Sharpness(img) #Contrast

# Applying the enhancer 
enhnaced_image = color_enhancer.enhance(0)
contrast_image = contrast_enhancer.enhance(5) 
bright_image = brightness_enhancer.enhance(5)
sharpen_image = sharpness_enhancer.enhance(5)
sharpen_image.show()