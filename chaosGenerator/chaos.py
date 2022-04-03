#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 14:21:54 2019

@author: alem
"""

#------------------------------------------------------------------------------
import math
import time
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import scipy.misc
import pylab as pl
from matplotlib import pyplot as mp
import cv2
#scipy.misc.imsave('outfile.jpg', image_array)
#------------------------------------------------------------------------------
start=time.time()
a=0.00489
var=5.98732516340
sn=5
mult=69621;
m=2147483647;
SoXIn=118811138160210142635318637165
SoYIn=11515410245191208781102411495549
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
b=math.sqrt(1-a**2);
Xo=var+SoXIn
Yo=var+SoYIn
#------------------------------------------------------------------------------
t1=9999+int(var)
t=np.arange(0.0, t1, 0.1)
X1 = np.array([(math.exp(a*t[i])*(Xo*math.cos(b*t[i])+
        1/b*(Yo-a*Xo)*math.sin(b*t[i]))) for i in range(len(t))])
Y1=np.array([(math.exp(a*t[i])*(Yo*math.cos(b*t[i])+
        a/b*(Yo-a*Xo-b**2/a*Xo)*math.sin(b*t[i]))) for i in range(len(t))])    


x=X1/(max(X1))
y=Y1/(max(Y1))
#------------------------------------------------------------------------------
dec=0
for i in range(sn):    
    plt.plot(x+i,y-dec)   
    dec=dec+0.1
    #plt.savefig('aa.png')
plt.savefig('chaos.png')
crop=cv2.imread('chaos.png')
h,w=crop.shape[:2]
x1=int(0.22*w)
y1=int(0.3*h)
crop1 = crop[y1:y1+int(h*0.4), x1:x1+int(w*0.58)]
#cv2.imwrite('mask.png',crop1)
resized_image=cv2.resize(crop1,(512,512))
cv2.imwrite('mask.png',resized_image)

end=time.time()
print("Time=",end-start)