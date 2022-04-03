#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:12:35 2019

@author: alem fitwi
"""
"""
Video processing
https://www.learnopencv.com/read-write-and-display-a-video-using-opencv-cpp-python/
"""
#============================================================================
import cv2
import numpy as np
import timeit
import time
#============================================================================
#Recommended video frame size w=640,h=480, program is based on this size
rgb_color=(0, 0, 0)
#haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('faces.xml')
img_1 = cv2.imread('aa2.jpg') #432x288
x=55
y=40
crop_img = img_1[y:y+208, x:x+332]
cv2.imwrite('./crop.jpg',crop_img)
mask=cv2.resize(crop_img,(640,480))
cv2.imwrite('./resized.jpg',mask)
cap = cv2.VideoCapture(0)
#============================================================================
#Saving the video
# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
# Define the fps to be equal to 10. Also frame size is passed.
frame_w=int(cap.get(3))
frame_h=int(cap.get(4))
out = cv2.VideoWriter('outpy1.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 
                          10, (frame_w,frame_h))
l=0
start = time.time()
while 1:    
    ret, img = cap.read()
    ret2,img4=cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    height, width = img.shape[:2]
    #========================================================================   
    color = tuple(reversed(rgb_color))
    image = np.zeros((width,height, 3), np.uint8)
    color = tuple(reversed(rgb_color))
    image[:] = color
    l_img=cv2.resize(image,(width,height))
    cv2.imwrite('./l_pic.jpg',l_img) 
    #========================================================================
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)   
        #====================================================================
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]        
        #====================================================================
        s_img = mask[y:y+h, x:x+w]
        l_img[y:y+h, x:x+w] = s_img       
        b = np.asarray(l_img)
        a = np.asarray(img)
        #====================================================================
        #Encryption
        img=np.bitwise_xor(a,b)
        cv2.imwrite('./xor13.jpg',img)        
        #Decryption
        img4=np.bitwise_xor(img,b) 
        cv2.imwrite('./xor23.jpg',img4)
        #====================================================================
        #roi_gray = gray[y:y+h, x:x+w]
        #roi_color = img[y:y+h, x:x+w]
        #====================================================================
    cv2.imwrite('/home/alem/computerVision/masking/frames/'+'xored_'+str(l)+'.jpg',img)
    out.write(img)
    cv2.imshow('Maksed Video',img)
    cv2.imshow('Unmasked Video',img4)
    #cv2.imshow('img',img4)    
    #Frames per second using video.get(cv2.CAP_PROP_FPS)
    fps = cap.get(cv2.CAP_PROP_FPS)
    print("Frames per second : {0}".format(fps))   
    end=time.time()
    print("end=",end)
    print("tot_time=",(end-start))
    l+=1
    k = cv2.waitKey(30) & 0xff
    if k == 27:        
        break
cap.release()
out.release()
cv2.destroyAllWindows()
