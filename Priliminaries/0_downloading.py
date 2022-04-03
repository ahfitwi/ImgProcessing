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

def store_negraw_images():
    #http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513    
    neg_images_link='http://image-net.org/api/text/imagenet.synset.geturls?wnid=n04326547'
    neg_image_urls=urllib.request.urlopen(neg_images_link).read().decode()
    if not os.path.exists('neg'):
        os.makedirs('neg')
    pic_num=1
    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, "neg1/"+str(pic_num)+'.jpg')
            img=cv2.imread("neg1/"+str(pic_num)+'.jpg',cv2.IMREAD_GRAYSCALE)
            resized_image=cv2.resize(img,(100,100))
            cv2.imwrite('neg/'+'wall_'+str(pic_num)+'.jpg',resized_image)
            pic_num+=1
        except Exception as e:
            print(str(e))
def store_posraw_images():    
    #http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152
    neg_images_link='http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152'
    pos_image_urls=urllib.request.urlopen(neg_images_link).read().decode()
    if not os.path.exists('pos'):
        os.makedirs('pos')
    pic_num=1
    for i in pos_image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, "pos/"+str(pic_num)+'.jpg')
            img=cv2.imread("pos/"+str(pic_num)+'.jpg',cv2.IMREAD_GRAYSCALE)
            resized_image=cv2.resize(img,(100,100))
            cv2.imwrite('pos/'+'win_'+str(pic_num)+'.jpg',resized_image)
            pic_num+=1
        except Exception as e:
            print(str(e))

store_negraw_images()
store_posraw_images()


def find_uglies():
    for file_type in ['neg']:
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
                        
def create_pos_n_neg():
    for file_type in['neg']:
        for img in os.listdir(file_type):
            if file_type=='neg':
                line=file_type+'/'+img+'\n'
                with open('bg.txt','a') as f:
                    f.write(line)
            elif file_type=='pos':
                line=file_type+'/'+img+' 1 0 0 50 50\n'
                with open('info.dat','a') as f:
                    f.write(line)
create_pos_n_neg()            
