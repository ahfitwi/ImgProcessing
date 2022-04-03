#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 22:35:06 2019

@author: alem
"""
#============================================================================
import cv2
from glob import glob   
#============================================================================
images = glob('./*.jpg')
for name in images:      
    img=cv2.imread(name)
    y=120
    x=200
    crop_img = img[y:y+128, x:x+128]
    cv2.imwrite('/home/alem/HaarPaperPrivacy/temp3/'+name,crop_img)     
    print("Croping")
#============================================================================