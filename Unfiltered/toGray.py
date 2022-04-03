# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 00:09:06 2019

@author: Alem
"""

#!/usr/bin/env python
from glob import glob                                                           
import cv2 
images = glob('./*.jpg')
for name in images:      
    img=cv2.imread('/home/alem/Desktop/privacy/PhD/0_Datasets/1_wallsRaw/ale1/'+name,cv2.IMREAD_GRAYSCALE)
    cv2.imwrite('/home/alem/Desktop/privacy/PhD/0_Datasets/1_wallsRaw/grey/'+name,img)      
    print("Graying")
