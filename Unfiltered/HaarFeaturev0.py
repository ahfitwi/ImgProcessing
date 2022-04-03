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
import math    
#============================================================================
#Recommended video frame size w=640,h=480, program is based on this size
face_cascade = cv2.CascadeClassifier('faces.xml')
cap = cv2.VideoCapture(0)
#============================================================================
start = time.time()
frame_count=1

while 1:    
    ret, frame = cap.read() 
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)    
    height, width = frame.shape[:2]
    #========================================================================   
    #========================================================================
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)   
        #====================================================================
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]   """     
        #====================================================================    
    #========================================================================  
    #End time
    end=time.time()
    tot_time=math.floor(end-start)    
    print("tot_time=",tot_time)
    if tot_time!=0:
        fps=math.ceil(frame_count/tot_time)
        print("fps=",fps)
    
    frame_count+=1
    cv2.imshow("Trial",frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:        
        break
    """
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
        """
cap.release()
cv2.destroyAllWindows()