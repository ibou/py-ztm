from PIL import Image, ImageFilter

img = Image.open('./image-playground/Pokedex/pikachu.jpg')
# filtered_image = img.filter(ImageFilter.SHARPEN)
filtered_image = img.convert('L')
box = (100, 100, 400, 400)
region = img.crop(box) 
region = img.resize((300,300))
region = region.transpose(Image.Transpose.ROTATE_90)
img.paste(region, box)
# resized_image.save('./image-playground/blur.png', 'png')
region.show()