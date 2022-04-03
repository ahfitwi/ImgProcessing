#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 23:40:13 2019

@author: alem
"""
import urllib.request
import cv2
import numpy as np
import os

def find_uglies():
    for file_type in ['wall']:
        for img in os.listdir(file_type):
            for ugly in os.listdir('uglies'):
                try:
                    current_image_path=str(file_type)+'/'+str(img)
                    ugly=cv2.imread('uglies/'+str(ugly))
                    question=cv2.imread(current_image_path)
                    
                    if ugly.shape==question.shape and not(np.bitwise_xor(ugly,question).any()):
                        print('Noisy pics')
                        print(current_image_path)
                        os.remove(current_image_path)
                except Exception as e:
                    print(str(e))
find_uglies()                   
           
