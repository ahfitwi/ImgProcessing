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
import time
import math    
#============================================================================
#Recommended video frame size w=640,h=480, program is based on this size
rgb_color=(0, 0, 0)
#haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('stage0.xml')
img_1 = cv2.imread('/home/alem/Desktop/privacy/PhD/5_Results/aa2.jpg')#432x288
x=55
y=40
crop_img = img_1[y:y+208, x:x+332]
cv2.imwrite('/home/alem/Desktop/privacy/PhD/5_Results/'+'crop.jpg',crop_img)
mask=cv2.resize(crop_img,(640,480))
cv2.imwrite('/home/alem/Desktop/privacy/PhD/5_Results/'+'resized.jpg',mask)
cap = cv2.VideoCapture("/home/alem/Desktop/privacy/PhD/5_Results/winvid.mp4")
#============================================================================
#Saving the video
# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
# Define the fps to be equal to 10. Also frame size is passed.
#frame_w=int(cap.get(3))
#frame_h=int(cap.get(4))
#path='/home/alem/Desktop/privacy/PhD/5_Results/winvid.mp4'
#out = cv2.VideoWriter(path,cv2.VideoWriter_fourcc('M','J','P','G'), 
                          #10, (frame_w,frame_h))
l=0
start=time.time()
frame_count=1
while 1:    
    ret, frame = cap.read()   
    ret2,img=cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if(len(faces)>=1):
        h1, w1 = frame.shape[:2]
        frame[h1-1,w1-3]=[255, 127, 1]
        frame[h1-1,w1-2]=[127, 1, 255]
        frame[h1-1,w1-1]=[1, 255, 127]
    height, width = frame.shape[:2]
    #========================================================================   
    color = tuple(reversed(rgb_color))
    image = np.zeros((width,height, 3), np.uint8)
    color = tuple(reversed(rgb_color))
    image[:] = color
    l_img=cv2.resize(image,(width,height))
    cv2.imwrite('/home/alem/Desktop/privacy/PhD/5_Results/'+'l_pic.jpg',l_img) 
    #========================================================================
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)   
        #====================================================================
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]        
        #====================================================================
        s_img = mask[y:y+h, x:x+w]
        l_img[y:y+h, x:x+w] = s_img       
        b = np.asarray(l_img)
        a = np.asarray(frame)
        #====================================================================
        #Encryption
        frame=np.bitwise_xor(a,b)
        #cv2.imwrite('./xor13.jpg',img)        
        #Decryption
        img=np.bitwise_xor(frame,b) 
        #cv2.imwrite('./xor23.jpg',img4)
        #====================================================================        
    #========================================================================
    #Saving video frames
    """cv2.imwrite('/home/alem/Desktop/privacy/PhD/5_Results/Frames/'+
                  'out_'+str(l)+'.jpg',frame)"""
    #Saving video with privacy enforced
    #out.write(frame)
    #Displaying masked and unmasked videos
    cv2.imshow('Maksed Video',frame)
    cv2.imshow('Unmasked Video',img)
    #========================================================================  
    #End time
    end=time.time()
    tot_time=math.floor(end-start)    
    print("tot_time=",tot_time)
    if tot_time!=0:
        fps=math.ceil(frame_count/tot_time)
        print("fps=",fps)
    l+=1
    frame_count+=1
    k = cv2.waitKey(30) & 0xff
    if k == 27:        
        break
    """if cv2.waitKey(0) & 0xFF == ord('q'):
        break"""
cap.release()
#out.release()
cv2.destroyAllWindows()
