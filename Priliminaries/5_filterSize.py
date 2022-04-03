# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 00:09:06 2019

@author: Alem
"""

#!/usr/bin/env python
from glob import glob                                                           
import cv2 
#========================
pngs = glob('./*.jpg')
for j in pngs:
    img = cv2.imread(j)    
    #cv2.imwrite(j[:3] + "Img"+str(i)+'.jpg', img)
    w = img.shape[1]
    h = img.shape[0] 
    if (h*w==16384):
        cv2.imwrite('/home/alem/HaarPaperPrivacy/wall/'+j, img)
    #cv2.imwrite('/home/alem/Desktop/windows/grayWins/'+name,img)    
    print("Filtering")
