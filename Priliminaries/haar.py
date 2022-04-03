#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:12:35 2019

@author: alem
"""
#https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/
#https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/
import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#this is the cascade we just made. Call what you want
#watch_cascade = cv2.CascadeClassifier('watchcascade10stage.xml')

cap = cv2.VideoCapture(0)
rgb_color=(0, 0, 0)
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #-----Beginning of the added snipet of code
    height, width = img.shape[:2]
    print("h=",height)
    print("w=",width)
    #========================================================================   
    color = tuple(reversed(rgb_color))
    image = np.zeros((width,height, 3), np.uint8)
    color = tuple(reversed(rgb_color))
    image[:] = color
    l_pic=cv2.resize(image,(width,height))
    cv2.imwrite('./l_pic01.jpg',l_pic) 
    #========================================================================
    # add this
    # image, reject levels level weights.
    #watches = watch_cascade.detectMultiScale(gray, 50, 50)
    
    # add this
    """for (x,y,w,h) in watches:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)"""

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        """eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)"""

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()