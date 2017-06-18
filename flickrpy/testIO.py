__author__ = "Shuai Chen <shuaic92@gmail.com>"
from PIL import Image
filename = './35235324831_11b168cdc4_b.jpg'
photo = Image.open(filename)
photo.save('test.jpg')