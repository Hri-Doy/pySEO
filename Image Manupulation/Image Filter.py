from PIL import Image, ImageFilter

#Image Import
image = Image.open('Image Manupulation/picture.jpg')

#Basic Filters
image_blur = image.filter(ImageFilter.BLUR)
image_contour = image.filter(ImageFilter.CONTOUR)
image_detail = image.filter(ImageFilter.DETAIL)
image_edge = image.filter(ImageFilter.EDGE_ENHANCE)
image_edge_moer = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
image_fild_edges = image.filter(ImageFilter.FIND_EDGES)
image_emboss = image.filter(ImageFilter.EMBOSS)
image_sharp = image.filter(ImageFilter.SHARPEN)
image_smooth = image.filter(ImageFilter.SMOOTH)
image_smooth_more = image.filter(ImageFilter.SMOOTH_MORE)

# Rank Filter:
image_filtered_min = image.filter(ImageFilter.MinFilter(size=15))
image_filtered_mediun = image.filter(ImageFilter.MedianFilter(size=5))
image_filtered_max = image.filter(ImageFilter.MaxFilter(size=15))


# Multiband
image_boxblur = image.filter(ImageFilter.BoxBlur(radius = 3))
image_gaussblur = image.filter(ImageFilter.GaussianBlur(radius=5))
image_unsharp = image.filter(ImageFilter.UnsharpMask(radius=5))


# Combined Filters
image_emboss = image.filter(ImageFilter.EMBOSS)
image_emboss_blur = image_emboss.filter(ImageFilter.GaussianBlur(radius=2))

# Seeing the filtered Image 
image_emboss_blur.show()