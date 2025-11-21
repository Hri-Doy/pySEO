# import os
# from PIL import Image
# images = os.listdir('Bulk Imgs Resize/imagess')
# print(images)
# for image in images:
#     img = Image.open('Bulk Imgs Resize/imagess/'+image)
#     w,h = img.size
#     width = 600
#     height = 315
#     # ratio = width/w
#     # height = int(ratio * h)
#     resized = img.resize((width, height))
#     resized.save('Bulk Imgs Resize/Resized'+image)
    
    
import os
from PIL import Image
images = os.listdir('Bulk Imgs Resize/imagess')
for image in images:
    img = Image.open('Bulk Imgs Resize/imagess/'+image)
    w,h = img.size
    #print(w,h)
    weight = 600
    ratio = weight / w
    #print(ratio)
    height = int(ratio * h)
    #print(height)
    resize = img.resize((weight,height))
    resize.save('Bulk Imgs Resize/Resized/'+image)