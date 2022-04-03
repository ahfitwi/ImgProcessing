#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 14:44:24 2019

@author: alem
"""

# importing required libraries of opencv 
import cv2 

# importing library for plotting 
from matplotlib import pyplot as plt 

# reads an input image 
img = cv2.imread('finalImage.jpg',0) 

# find frequency of pixels in range 0-255 
histr = cv2.calcHist([img],[0],None,[256],[0,256]) 
plt.hist(img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k') #calculating histogram

# show the plotting graph of an image 
plt.plot(histr) 
plt.show() 