#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 15:08:14 2019

@author: alem
"""
#! /usr/bin/env python3
from PIL import Image
import random
import time

start=time.time()
def drawImage():
    testImage = Image.new("RGB", (224,224), (255,255,255))
    pixel = testImage.load()
    for x in range(224):
        for y in range(224):
            red = random.randrange(0,255)
            blue = random.randrange(0,255)
            green = random.randrange(0,255)
            pixel[x,y]=(red,blue,green)
    return testImage
def main():
    finalImage = drawImage()
    finalImage.save("chaoticRandom.jpg")
if __name__ == "__main__":
    main()
end=time.time()
print("Time=",end-start)