#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 04:53:40 2019

@author: alem
"""

import os
#Create the file descriptor
def create_descriptor():
    k=1
    for file_type in ['/home/alem/Desktop/privacy/test/allinfo/']:        
        for img in os.listdir(file_type):
            with open("bg.txt", "r") as ins:
                lines = []
        for line in ins:
            lines.append(line)
            line = file_type+'/'+img+'\n'
                with open('bg.txt','a') as f:
                    f.write(line)

create_descriptor()

with open("sn.txt", "r") as ins:
        lines = []
        for line in ins:
            lines.append(int(line))
lst=[]
p=1
for i in range(1,2):
    path='/home/alem/Desktop/privacy/test/allinfo/info'+str(k)+'/inf0'+str(i)+'.lst'
    with open(path, "r") as ins:
        lines = []
        for line in ins:
            temp=sn[p]+line[4:len(line)])
            lines.append(temp)

s = 'Don Quijote'
t=str(0000)+s[3:11]
print("0000"+s[3:11])

r='0001_0024_0034_0053_0053.jpg 1 24 34 53 53'
print("00001"+r[4:len(r)])
#creating combined list
sn=[]
for k in range(1,11601):
    if k<10:
        line='0000'+ str(k)
    elif k>=10 and k<100:
        line='000'+ str(k)
    elif k>=100 and k<1000:
        line='00'+ str(k)
    elif k>=1000 and k<10000:
        line='0'+ str(k)
    else:
        line=str(k)
    sn.append(line) 
lines=[]
p=0
for i in range(1,581):
    path='/home/alem/Desktop/privacy/test/allinfo/info'+str(i)+'/info'+str(i)+'.lst'
    with open(path, "r") as ins:        
        for line in ins:
            temp=sn[p]+line[4:len(line)]
            lines.append(temp)
            p+=1

k=1	
for jj in range(11600):
    line =lines[jj]
    with open('info.lst','a') as f:
        f.write(line)          
#=========================================================================
sn=[]
for k in range(1,11601):
    if k<10:
        line='0000'+ str(k)
    elif k>=10 and k<100:
        line='000'+ str(k)
    elif k>=100 and k<1000:
        line='00'+ str(k)
    elif k>=1000 and k<10000:
        line='0'+ str(k)
    else:
        line=str(k)
    sn.append(line) 
lines=[]
p=0
for i in range(1,581):
    path='/home/alem/Desktop/privacy/test/allinfo/info'+str(i)+'/'
    
    with open(path, "r") as ins:        
        for line in ins:
            temp=sn[p]+line[4:len(line)]
            lines.append(temp)
            p+=1

k=1	
for jj in range(11600):
    line =lines[jj]
    with open('info.lst','a') as f:
        f.write(line)          