# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 00:09:06 2019

@author: Alem
"""

#!/usr/bin/env python
from glob import glob                                                           
import cv2 
images = glob('/home/alem/Desktop/privacy/PhD/0_Datasets/1_wallsRaw/temp/*.jpg')
for name in images:      
    img=cv2.imread('/home/alem/Desktop/privacy/PhD/0_Datasets/1_wallsRaw/temp'+name,cv2.IMREAD_GRAYSCALE)
    cv2.imwrite('/home/alem/Desktop/privacy/PhD/0_Datasets/TrainingSet/wall_gray/'+name,img)      
    print("Graying")