from PIL import Image, ImageFilter, ImageOps

image = Image.open("sample.jpg")

grayscale = ImageOps.grayscale(image)
grayscale.save("grayscale.jpg")

blurred = image.filter(ImageFilter.BLUR)
blurred.save("blurred.jpg")

inverted = ImageOps.invert(image)
inverted.save("inverted.jpg")

print("Filters applied successfully.")
