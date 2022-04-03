#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 08:53:00 2019

@author: alem
"""

import cv2 
img = cv2.imread('labeledwinsFaces.jpg')   
resized_image=cv2.resize(img,(224,224))
cv2.imwrite('labeledwinsFacesr.jpg',resized_image)      
    