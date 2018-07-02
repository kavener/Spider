import tesserocr
from PIL import Image
image = Image.open("image.png")
print(tesserocr.image_to_text(image))
print("New Pro.")
print("把一件事情做到极致，即专研爬虫！！！")