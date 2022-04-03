# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 00:09:06 2019

@author: Alem
"""

#!/usr/bin/env python
from glob import glob                                                           
import cv2 
images = glob('./*.jpg')
for j in images:
    img = cv2.imread(j)   
    resized_image=cv2.resize(img,(128,128))
    cv2.imwrite('/home/alem/HaarPaperPrivacy/wall/'+j,resized_image)      
    print("Resizing")