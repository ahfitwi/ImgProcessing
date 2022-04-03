import os
from PIL import Image
from glob import glob                                                           
#import cv2 
files = glob('./*.jpg')

"""files = [
  '~/Downloads/1.jpg',
  '~/Downloads/2.jpg',
  '~/Downloads/3.jpg',
  '~/Downloads/4.jpg']"""

result = Image.new("RGB", (4096,4096))

for index, file in enumerate(files):
  path = os.path.expanduser(file)
  img = Image.open(path)
  img.thumbnail((128, 128), Image.ANTIALIAS)
  x = index // 32 * 128
  y = index % 32 * 128
  w, h = img.size
  #print('pos {0},{1} size {2},{3}'.format(x, y, w, h))
  result.paste(img, (x, y, x + w, y + h))

result.save(os.path.expanduser('mosaic.jpg'))