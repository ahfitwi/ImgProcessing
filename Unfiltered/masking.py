#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 02:02:26 2019

@author: alem
"""
#============================================================================
import cv2
import numpy as np
from PIL import Image
#============================================================================
path='/home/alem/computerVision/logical/'
img1=cv2.imread(path+'bab.jpg')
img11=cv2.resize(img1,(345,235))
cv2.imwrite('img11.jpg',img11)
#============================================================================
rgb_color=(0, 0, 0)
color = tuple(reversed(rgb_color))
image = np.zeros((345, 235, 3), np.uint8)
color = tuple(reversed(rgb_color))
image[:] = color
l_pic=cv2.resize(image,(345,235))
cv2.imwrite('./l_pic.jpg',l_pic) 
#============================================================================
im = Image.open('aa2.jpg')
img = cv2.imread('aa2.jpg')
w, h = im.size
#y=int((h-64)/2)-20
#x=int((w-64)/2)-20
x=125
y=60
#============================================================================
crop_img = img[y:y+120, x:x+120]
cv2.imwrite('./crop.jpg',crop_img) 
s_img = cv2.imread("crop.jpg")
x=120
y=60
l_pic[y:y+120, x:x+120] = s_img
cv2.imwrite('./l_pic01.jpg',l_pic) 
b = np.asarray(l_pic)
a = np.asarray(img11)
#============================================================================
#Encryption
t=np.bitwise_xor(a,b)
cv2.imwrite('./xor.jpg',t)
#Decryption
img4=np.bitwise_xor(t,b) 
cv2.imwrite('./xor2.jpg',img4)
#============================================================================
