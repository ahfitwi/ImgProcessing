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
cap = cv2.VideoCapture(0)
#============================================================================
frame_w=int(cap.get(3))
frame_h=int(cap.get(4))
out = cv2.VideoWriter('faces.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 
                          10, (frame_w,frame_h))
c=0
t2=0
start=time.time()
while 1:    
    ret, frames = cap.read()     
    if ret and t2<=15:
        c+=1
        #frames=cv2.resize(frames,(720,405))
        out.write(frames)
        cv2.imshow('frames',frames)          
        if cv2.waitKey(1) & 0xff==ord('q'):
            break
    else:
        break
    end1=time.time()
    t2=end1-start
end=time.time()
t=end-start
print("The attained fps=",int(c/t))
cap.release()
out.release()
cv2.destroyAllWindows()