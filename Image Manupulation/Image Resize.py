from PIL import Image
img = Image.open('Image Manupulation/picture.jpg')
#img.show()
data = img.getdata()
#print(list(data))
#print(img.size)
width, height = img.size
# print('Width', width)
# print('Height', height)
# new_img = img.resize((720,480))
# new_img.save('Image Manupulation/Resized.jpg')
#new_img.show()

new_width = 690
ratio = new_width/width
new_height = int(height*ratio)
new_img = img.resize((new_width, new_height))
new_img.save('Image Manupulation/Ratio.jpg')
