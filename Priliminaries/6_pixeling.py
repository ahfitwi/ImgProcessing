#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 05:52:56 2019

@author: alem
"""

import cv2
import numpy as np
#At the edge, camera
image = cv2.imread("2.jpg")
h, w = image.shape[:2]
image[h-1,w-3]=[255, 127, 1]
image[h-1,w-2]=[127, 1, 255]
image[h-1,w-1]=[1, 255, 127]
cv2.imwrite('/home/alem/HaarPaperPrivacy/TrainingSet/wall/'+'wall0.jpg',image)
#At the receiving end
ima = cv2.imread("wall0.jpg")
h, w = ima.shape[:2]
t1=np.all(image[h-1,w-3]==[255, 127, 1])
t2=np.all(image[h-1,w-2]==[127, 1, 255])
t3=np.all(image[h-1,w-1]==[1, 255, 127])
#=============================================================================
if (t1 and t2 and t3):
    print('True') 
