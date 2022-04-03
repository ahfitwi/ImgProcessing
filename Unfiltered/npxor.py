#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 01:11:30 2019

@author: alem
"""
import math
import numpy as np
import cv2
import bpy

def np_array_from_image(img_name):
    img = bpy.data.images[img_name]
    return np.array(img.pixels[:])
#===========================================
img1 = cv2.imread("bab.jpg")
img1=cv2.resize(img1,(345,235))
a = np.asarray(img1)

#-------------------
rgb_color=(0, 0, 0)
color = tuple(reversed(rgb_color))
image = np.zeros((345, 235, 3), np.uint8)
color = tuple(reversed(rgb_color))
image[:] = color
l_pic=cv2.resize(image,(345,235))
b = np.asarray(l_pic)
cv2.imwrite('./l_pic.jpg',l_pic) 

t=np.bitwise_xor(a,b)
cv2.imwrite('color_img.jpg', t)
#==========================================
pixelsA = np_array_from_image('A')
pixelsB = np_array_from_image('B')
pixelsC = np_array_from_image('C')
pixelsD = (pixelsA + pixelsB + pixelsC) / 3

image_D = bpy.data.images['D']
image_D.pixels = pixelsD.tolist()
np.bitwise_xor