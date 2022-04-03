#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 20:28:35 2019

@author: alem
"""
#Learn Computer Vision with OpenCV Library using Python --> Udemy
#--------------------------------------------------------------------------
#1.Image Fundamentals
#-------------------
#--------------------------------------------------------------------------
#Image reading
import numpy as np
import cv2
img1=cv2.imread('fig_4.jpg') # Display as it is
img2=cv2.imread('fig_4.jpg',0) #Display gray image
cv2.imshow('Win', img1)
cv2.imshow('Wall', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Checked --> works fine
#--------------------------------------------------------------------------
#Image saving
import numpy as np
import cv2
img1=cv2.imread('fig_4.jpg') 
img2=cv2.imwrite('saved1.jpg',img1) 
img3=cv2.imread('saved1.jpg') 
cv2.imshow('Saved', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Checked --> works fine
#--------------------------------------------------------------------------
#2.Drawing shape and writing text on an image
#-------------------
#--------------------------------------------------------------------------
#Drawing a Rectangle
import numpy as np
import cv2
pic = np.zeros((500,500,3), dtype='uint8')
#pic2 = np.ones((500,500,3))
cv2.rectangle(pic, (0,0),(150,150),(123,200,98), 3, lineType=8, shift=0)
                   #start  width, height
cv2.imshow('dark', pic)
#cv2.imshow('dark', pic2)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Checked --> works fine
#--------------------------------------------------------------------------
#Drawing a line
import numpy as np
import cv2
pic = np.zeros((500,500,3), dtype='uint8')
cv2.line(pic, (350,350),(500,350),(0,0,255))
             # start     end       color
cv2.imshow('dark', pic) 
cv2.waitKey(0)
cv2.destroyAllWindows()
#Checked --> works fine
#--------------------------------------------------------------------------
#Drawing a circle
import numpy as np
import cv2
pic = np.zeros((500,500,3), dtype='uint8')
color=(255,0,255)
cv2.circle(pic, (250,250),150,color)
               #center  radius    
cv2.imshow('dark', pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Checked --> works fine
#--------------------------------------------------------------------------
#Writing text
import numpy as np
import cv2
pic = np.zeros((500,500,3), dtype='uint8')
font=cv2.FONT_HERSHEY_DUPLEX
cv2.putText(pic, 'SUNY', (100,100), font, 3, (255,255,255), 4, cv2.LINE_8)
                                          #    B   G   R
cv2.imshow('dark', pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Checked --> works fine
#--------------------------------------------------------------------------
#Drawing combination: Line, Rectangle, circle, and Text
import numpy as np
import cv2
pic = np.zeros((500,500,3), dtype='uint8')
cv2.rectangle(pic, (0,0),(500,150),(123,200,98), 3, lineType=8, shift=0)
font=cv2.FONT_HERSHEY_DUPLEX
cv2.putText(pic, 'BU', (100,100), font, 3, (255,255,255), 4, cv2.LINE_8)
cv2.circle(pic, (250,250),50,(255,0,255))
cv2.line(pic, (133,138),(388,133),(0,0,255))
cv2.imshow('dark', pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Checked --> works fine
#--------------------------------------------------------------------------
#3.Image Processing
#-------------------
#--------------------------------------------------------------------------
#Image Transformations
import numpy as np
import cv2
pic=cv2.imread('saved1.jpg')
cols=pic.shape[1]
rows=pic.shape[0]

M=np.float32([[1,0,150],[0,1,170]])
#M=np.float32([[1,0,-150],[0,1,-170]])
shifted=cv2.warpAffine(pic,M,(cols,rows))
cv2.imshow('shifted',shifted)

cv2.waitKey(0)
cv2.destroyAllWindows()
#Checked --> works fine
#--------------------------------------------------------------------------
#Image Rotation
import numpy as np
import cv2
pic=cv2.imread('saved1.jpg')
cols=pic.shape[1]
rows=pic.shape[0]
center=(cols/2,rows/2)
angle=90
#angle=-90
M=cv2.getRotationMatrix2D(center,angle,1)
rotate=cv2.warpAffine(pic,M,(cols,rows))
cv2.imshow('rotated',rotate)

cv2.waitKey(0)
cv2.destroyAllWindows()
#Checked --> works fine
#--------------------------------------------------------------------------
# Image Thresholding
import numpy as np
import cv2
pic=cv2.imread('saved1.jpg')
threshold_val=150
(T_value,binary_threshold)=cv2.threshold(pic,threshold_val, 255, cv2.THRESH_BINARY)
cv2.imshow('Binary',binary_threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()
#Checked --> works fine
#--------------------------------------------------------------------------
#4.Image Filtering
#-------------------
#--------------------------------------------------------------------------
#Guassion Blur
import numpy as np
import cv2
pic=cv2.imread('saved1.jpg')
matrix=(7,7)
blur=cv2.GaussianBlur(pic,matrix,0)
cv2.imshow('blurred',blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Checked --> works fine
#--------------------------------------------------------------------------
#Median Blur
import numpy as np
import cv2
pic=cv2.imread('saved1.jpg')
kernel=3
median=cv2.medianBlur(pic,kernel)
cv2.imshow('median',median)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Checked --> works fine
#--------------------------------------------------------------------------
#Bilateral Filtering
import numpy as np
import cv2
pic=cv2.imread('saved1.jpg')
dimpixel=7
color=100
space=100
filter=cv2.bilateralFilter(pic,dimpixel,color,space)
cv2.imshow('filter',filter)
cv2.waitKey(0)
cv2.destroyAllWindows()
#--------------------------------------------------------------------------
#5.Feature Detection
#-------------------
#--------------------------------------------------------------------------
# Canny Edge Detector
import cv2
import numpy as np
pic = cv2.imread('saved1.jpg')

thresholdval1=50
thresholdval2=100

canny=cv2.Canny(pic,thresholdval1,thresholdval2)
cv2.imshow('canny',canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
#--------------------------------------------------------------------------
#6.Video Analysis
#-------------------
#--------------------------------------------------------------------------
# Load Video
import cv2
import numpy as np
cap=cv2.VideoCapture('sample.mp4')
while(cap.isOpened()):
    ret,frame=cap.read()
    cv2.imshow('vid', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
#--------------------------------------------------------------------------
# Save video in a different format
import cv2
import numpy as np
cap=cv2.VideoCapture('sample.mp4')
fourcc=cv2.VideoWriter_fourcc(*'XVID')
fps=30
framesize=(720,480)
out=cv2.VideoWriter('sample.avi',fourcc,fps,framesize)
while(cap.isOpened()):
    ret,frame=cap.read()
    cv2.imshow('vid', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
#--------------------------------------------------------------------------
#7.Applications
#-------------------
#--------------------------------------------------------------------------
# Introduction to image face detection
#Face detection by using Haar feature based cascade classifiers
#--------------------------------------------------------------------------
# Real time face detection using webcam
import cv2
import numpy as np
#https://github.com/Itseez/opencv/tree/master/data/haarcascades
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
videocapture=cv2.VideoCapture(0)
scale_factor=1.3
while 1:
    ret, pic=videocapture.read()
    faces=face_cascade.detectMultiScale(pic, scale_factor, 5)
    for(x,y,w,h) in faces:
        cv2.rectangle(pic,(x,y),(x+w,y+h),(255,0,0),2)
        font=cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(pic,'Alem', (x,y),font, 2, (255,255,255), 2, cv2.LINE_AA)
    print("Number_of_faces_found {}".format(len(faces)))
    cv2.imshow('face',pic)
    k=cv2.waitKey(30) &0xff
    if k==2:
        break
cv2.destroyAllWindows()
#--------------------------------------------------------------------------
# Image face detection
import cv2
import numpy as np
#https://github.com/Itseez/opencv/tree/master/data/haarcascades
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
pic=cv2.imread('shim.jpg')
scale_factor=1.3
while 1:   
    faces=face_cascade.detectMultiScale(pic, scale_factor, 5)
    for(x,y,w,h) in faces:
        cv2.rectangle(pic,(x,y),(x+w,y+h),(255,0,0),2)
        font=cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(pic,'Shime', (x,y),font, 2, (255,255,255), 2, cv2.LINE_AA)
    print("Number_of_faces_found {}".format(len(faces)))
    cv2.imshow('face',pic)
    k=cv2.waitKey(30) &0xff
    if k==2:
        break
cv2.destroyAllWindows()
#--------------------------------------------------------------------------
#  Real Image face detection using webcam
import cv2
import numpy as np
#https://github.com/Itseez/opencv/tree/master/data/haarcascades
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

videocapture=cv2.VideoCapture(0)
scale_factor=1.3
while 1:
    ret, pic=videocapture.read()
    faces=face_cascade.detectMultiScale(pic, scale_factor, 5)
    for(x,y,w,h) in faces:
        cv2.rectangle(pic,(x,y),(x+w,y+h),(255,0,0),2)
        font=cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(pic,'Me', (x,y),font, 2, (255,255,255), 2, cv2.LINE_AA)
    print("Number_of_faces_found {}".format(len(faces)))
    cv2.imshow('face',pic)
    k=cv2.waitKey(30) &0xff
    if k==2:
        break
    fps = videocapture.get(cv2.CAP_PROP_FPS)
    print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
     
cv2.destroyAllWindows()
#--------------------------------------------------------------------------
#Logical Operators
import cv2
import matplotlib.pyplot as plt
import numpy as np
path='/home/alem/computerVision/logical/'
img1=cv2.imread(path+'bab.jpeg')
cv2.imwrite('/home/alem/computerVision/logical/'+'bab.jpg',img1) 
img1=cv2.imread(path+'bab.jpg')
img11=cv2.resize(img1,(345,235))
img2=cv2.imread(path+'baby2.png')
img22=cv2.resize(img2,(345,235))
#img21=cv2.cvtColor(img11,cv2.COLOR_BGR2GRAY)
cv2.imwrite('/home/alem/computerVision/logical/'+'img11.jpg',img11)
#img32=cv2.cvtColor(img22,cv2.COLOR_BGR2GRAY)
#l_pic = np.ones((235,345,3))#h,w
#l_pic=cv2.cvtColor(img42,cv2.COLOR_BGR2GRAY)
#cv2.imwrite('./l_pic1.jpg',l_pic) 
rgb_color=(0, 0, 0)
color = tuple(reversed(rgb_color))
image = np.zeros((345, 235, 3), np.uint8)
color = tuple(reversed(rgb_color))
image[:] = color
#img20=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
l_pic=cv2.resize(image,(345,235))
cv2.imwrite('./l_pic.jpg',l_pic) 
#===========================================
from PIL import Image
im = Image.open('aa2.png')
img = cv2.imread('aa2.png')
w, h = im.size
y=int((h-64)/2)-20
x=int((w-64)/2)-20
#spic = img[y:y+120, x:x+120]
crop_img = img[y:y+120, x:x+120]
#gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('./crop.jpg',crop_img) 
s_img = cv2.imread("crop.jpg")
#s_img=cv2.cvtColor(s_img,cv2.COLOR_BGR2GRAY)
x=120
y=55
l_pic[y:y+120, x:x+120] = s_img
cv2.imwrite('./l_pic.jpg',l_pic) 
#spic=cv2.imread('a.jpg') 
b = np.asarray(l_pic)
a = np.asarray(img11)
#Encryption
t=np.bitwise_xor(a,b)
#img3=cv2.bitwise_xor(a,b)
cv2.imwrite('./xor.jpg',t)
#Decryption
img4=np.bitwise_xor(t,b) 
cv2.imwrite('./xor2.jpg',img4)


img5=cv2.cvtColor(img4,cv2.COLOR_GRAY2RGB)
cv2.imwrite('./xor3.jpg',img5)

titles=['Image 1', 'Image 2', 'Image 1','Image 4']
images=[img1,img2,img3,l_pic]

for i in range(4):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
def main():
    path='/home/alem/computerVision/logical/'
    img1=path+'baby1.png'
    img2=path+'baby2.png'
    img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
    img3=cv2.bitwise_xor(img1,img2)
    titles=['Image 1', 'Image 2', 'Image 1']
    images=[img1,img2,img3]
    for i in range(3):
        plt.subplot(2,3,i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()
#--------------------------------------------------------------------------