import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
from os import listdir
from os.path import join, isfile
import glob

image_list = []
for filename in glob.glob('/path/*.png'): #dataset folder location and image type
    im=Image.open(filename)
    image_list.append(im)
    
n = len(image_list)
print(n)

for n in image_list: 
  text = pytesseract.image_to_string(n, lang="ben")
  print(text)
