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
import time
#============================================================================
cap = cv2.VideoCapture("VID_20190430_163239.3gp")
#cap = cv2.VideoCapture(0)
#============================================================================
#Saving the video
# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
# Define the fps to be equal to 10. Also frame size is passed.

l=1772
start = time.time()
while 1:    
    ret, img = cap.read() 
    resized_image=cv2.resize(img,(640,512))
    cv2.imwrite('./temp1/'+'frame_'+str(l)+'.jpg',resized_image)
    print("breaking")    
    cv2.imshow('Maksed Video',img)    
    l+=1
    """ end=time.time()
    diff=int(end-start)
    if diff>50:
        break"""
    k = cv2.waitKey(30) & 0xff
    if k == 27:        
        break
cap.release()
cv2.destroyAllWindows()
