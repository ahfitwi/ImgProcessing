#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 14:59:18 2019

@author: alem
"""

import cv2 
from matplotlib import pyplot as plt 
img = cv2.imread('finalImage.jpg',0) 

# alternative way to find histogram of an image 
plt.hist(img.ravel(),256,[0,256]) 
plt.show() 