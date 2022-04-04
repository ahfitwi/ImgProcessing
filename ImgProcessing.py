#--------------------------------------------------------------------------
# Image Processing
#--------------------------------------------------------------------------
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 20:28:35 2019

@author: alem
"""
#--------------------------------------------------------------------------
# Import All Necessary Python Modules Related to Image Processing
#--------------------------------------------------------------------------
import os
from socket import inet_pton
import sys
import glob
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

#--------------------------------------------------------------------------
class ImgProcessing:
    # ---------------------------------------------------------------------
    # Constructor Dunder Method
    # ---------------------------------------------------------------------
    def __init__(self, in_path = None, out_path = None):
        self.in_path = in_path
        self.out_path = out_path
    # ---------------------------------------------------------------------
    # Image Fundamentals
    # ---------------------------------------------------------------------
    #----------------------------------------------------------------------
    def cv3read_img(self, img_name, flag):
        """ Reads image using cv2 from in_path + img_name location"""
        #flag = 0, or cv2.IMREAD_GRAYSCALE for gray & 1/-1 as-is
        return cv2.imread(os.path(self.in_path, img_name))

    #----------------------------------------------------------------------
    def pilread_img(self, img_name):
        """ Reads image using PIL from in_path + img_name location"""
        return Image.open(os.path(self.in_path, img_name))

    #----------------------------------------------------------------------
    def cv3write_img(self, img, img_name):
        """ Writes image using cv2 to out_path + img_name location"""
        cv2.imwrite(os.path(self.out_path, img_name), img)

    #----------------------------------------------------------------------
    def pilwrite_img(self, img, img_name):
        """ Saves image using PIL from in_path + img_name location"""
        img.save(os.path.join(self.out_path, img_name))

    #----------------------------------------------------------------------
    def cv2show_img(self, img, title):
        """ Displays image using cv2"""
        cv2.imshow(title, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    #----------------------------------------------------------------------
    def pilshow_img(self, img):
        """ Displays image using PIL."""
        img.show()

    #----------------------------------------------------------------------
    def cv2get_Imgsize(self, img):
        """Returns H, W, & m of an image using cv2 in order."""
        return img.shape

    #----------------------------------------------------------------------
    def pilget_Imgsize(self, img):
        """Returns W & H of an image using PIL in order."""
        return img.size

    #----------------------------------------------------------------------
    def cv2resize_img(self, img, H, W):
        """Resizes input image using cv2"""
        return cv2.resize(img, (H,W))

    #----------------------------------------------------------------------
    def cv2resize_img(self, img, W, H):
        """Resizes input image using PIL"""
        return img.resize((W,H))

    #---------------------------------------------------------------------
    def grab_ImgNames(self):
        "Grabs the paths of images stored in ..."
        path1 = glob.glob(self.in_path + '*.jpg')
        path2 = glob.glob(self.in_path + '*.png')
        path3 = glob.glob(self.in_path + '*.jpeg')
        return path1 + path2 + path3

    #---------------------------------------------------------------------
    def create_Img(self, size:tuple, rgb_color:tuple):
        "Creates an Image"
        image = np.zeros(size, np.uint8)
        color = tuple(reversed(rgb_color))
        image[:] = color
        return image
        
    # ---------------------------------------------------------------------
    # Drawing shapes and writing texts on Images
    # ---------------------------------------------------------------------
    def draw_line(self, img, start:tuple, end:tuple, color:tuple, size:int):
        """Draws a line on an image"""
        cv2.line(img, start, end, color, size)
        return img

    #----------------------------------------------------------------------
    def draw_triangle(self, img, points:tuple, color:tuple, size:int):
        """Draws a triangle on an image"""
        # points = ((100, 200), (50,50), (300,100))
        cv2.line(img, points[0], points[1], color, size)
        cv2.line(img, points[0], points[2], color, size)
        cv2.line(img, points[1], points[2], color, size)
        return img

    #----------------------------------------------------------------------
    def draw_rectangle(self, img, start:tuple, end:tuple, color:tuple, 
                        size:int, lineType=8, shift=0):
        """Draws a rectangle on an image"""
        cv2.rectangle(img, start, end, color, size, 
                              lineType = lineType, shift=shift)
        return img

    #----------------------------------------------------------------------
    def draw_circle(self, img, center:tuple, radius:int, color:tuple, size:int):
        """Draws a circle on an image"""
        cv2.circle(img, center, radius, color, size)
        return img

    #----------------------------------------------------------------------
    def draw_polygon(self, img, pts, isClosed, color, size):
        "Draws a polygon with an array of corner-points"
        cv2.polylines(img, [pts], isClosed, color, size)
        return img

    #----------------------------------------------------------------------
    def add_txt(self, img, txt, start, font, ftype, color, fsize, ltype):
        """Adds text to an image"""
        # font=cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(img, txt, start, font, ftype, color,fsize, ltype)
        return img

    #----------------------------------------------------------------------
    # Image Processing
    #----------------------------------------------------------------------
    def warp_img(self, img, M:np.float32, pos:tuple):
        """Performs warpaffine on an Image"""
        # pos = (cols, rows)
        # M=np.float32([[1,0,rows//2],[0,1,cols//2]])
        return cv2.warpAffine(img, M, pos)

    #----------------------------------------------------------------------
    def rotate_img(self, img, center:tuple, angle, col, row, direction):
        """Rotates an image"""
        # direction --> 1 for CCW, -1 for CW
        M = cv2.getRotationMatrix2D(center, angle, direction)
        return cv2.warpAffine(img, M, (col, row))

    #----------------------------------------------------------------------
    def cv2ToGray(self, coloredImg):
        """Converts RGB image to grayscale"""
        #cv2.imread(path, 0)
        #cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        #cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return cv2.cvtColor(coloredImg, cv2.COLOR_BGR2GRAY)

    #----------------------------------------------------------------------
    def cv2Gray2BW(self, grayImg, th_val=127, m=cv2.THRESH_BINARY):
        """Converts grayscale img to black-and-white img, thresholding"""
        # m = cv.THRESH_BINARY_INV, cv.THRESH_TRUNC, cv.THRESH_TOZERO,
        #     cv.THRESH_TOZERO_INV
        return cv2.threshold(grayImg, th_val, 255, m)[1]
    
    #----------------------------------------------------------------------
    def shw_all_BW(self, img):
        """Converts img to black-and-white img using all methods"""
        ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
        ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
        ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
        ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
        ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
        titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO',
                                                          'TOZERO_INV']
        images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
        for i in range(6):
            plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
            plt.title(titles[i])
            plt.xticks([]),plt.yticks([])
        plt.show()

    #----------------------------------------------------------------------
    # Image Filtering
    #----------------------------------------------------------------------
    def gaussian_blur(self, img, ks:tuple, borderType=cv2.BORDER_DEFAULT):
        """Performs Gaussian Filtering"""
        #dst = cv2.GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, 
        #      borderType=BORDER_DEFAULT]]] )
        return cv2.GaussianBlur(img, ks, borderType)

    #----------------------------------------------------------------------
    def median_blur(self, img, ks:int):
        """Performs Median Filtering"""
        return cv2.medianBlur(img,ks)
    
    #----------------------------------------------------------------------
    def bilateral_blur(self, img, dimpixel:int, color:int, space:int):
        """Performs Bilateral Filtering"""
        return cv2.bilateralFilter(img,dimpixel,color,space)
    
    #----------------------------------------------------------------------
    # Feature Detection
    #----------------------------------------------------------------------
    def edge_detect_canny(self, img, thv1=100, thv2=200):
        """Detects edges/lines on an image"""
        return cv2.Canny(img,thv1,thv2)
    
    #----------------------------------------------------------------------
    def edge_detect_sobel(self, img_blur, ks:int):
        """Sobel Edge Detection"""
         # Sobel Edge Detection on the X axis
        sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, 
                                                                ksize=5)
        # Sobel Edge Detection on the Y axis
        sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, 
                                                                ksize=5) 
        # Combined X and Y Sobel Edge Detection
        sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, 
                                                                ksize=5) 
        return sobelxy
    
    #----------------------------------------------------------------------
    def find_contours(self, img, thv=127):
        """Returns the end points of contours"""
        # cv.CHAIN_APPROX_NONE: returns all points
        imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(imgray, thv, 255, 0)
        tmp=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        return tmp[0]
    
    #----------------------------------------------------------------------
    def draw_contours(self, img, cnts, flag, color:tuple, size):
        """Draws contours on an image"""
        #flag: -1 for all, val for index of one, or 0
        cv2.drawContours(img, cnts, flag, color, size)
        return img
    
    #----------------------------------------------------------------------
    #fcnts = [c for c in cnts if ins.filter_contours(c, H, W, sides)==True]
    def filter_contours(self, cnt, H, W, sides, ep=0.01, ap=0.000005, 
                        flag=True):
        # define contour approx. and hull
        epsilon = ep*cv2.arcLength(cnt,flag) 
        approx = cv2.approxPolyDP(cnt,epsilon, flag)
        #print(cv2.contourArea(approx), ap*H*W)
        if cv2.contourArea(approx)> ap*H*W and len(approx == sides):
            return True
        else:
            return False

    #----------------------------------------------------------------------
    def read_vid(self, vid_name):
        """Reads video frames."""
        path = os.path.join(self.in_path, vid_name)
        cap=cv2.VideoCapture(path)
        while(cap.isOpened()):
            ret,frame=cap.read()
            cv2.imshow('vid', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
        
    #----------------------------------------------------------------------
    def write_vid(self, vid_name_in, vid_name_out, framesize:tuple, fps=30):
        """Save vid in d/t format,  mp4 --> avi"""
        in_path = os.path.join(self.in_path, vid_name_in)
        out_path = os.path.join(self.out_path, vid_name_out)
        ccap=cv2.VideoCapture(in_path)
        fourcc=cv2.VideoWriter_fourcc(*'XVID')
        out=cv2.VideoWriter(out_path,fourcc,fps,framesize)
        while(cap.isOpened()):
            ret,frame=cap.read()
            cv2.imshow('vid', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()    
        
    #----------------------------------------------------------------------
    def crop_image(self, img, x, y, w, h):
        "Crops an image in x and y directions"
        return img[y:y+h, x:x+w]
    
    #----------------------------------------------------------------------
    def crop_irr_shape(self, img, points:np.array, pixel:int):
        "Crops an irregular shape from image"
        # points = np.array([[[10,150],[150,100],[300,150],[350,100],
        #                                             [310,20],[35,10]]])
        h, w = img.shape[:2]
        maskb = np.zeros((h, w), dtype=np.uint8)
        #maskw = np.zeros((h, w), dtype=np.uint8)
        #maskw.fill(255)
        cv2.fillPoly(maskb, points, (pixel))
        resb = cv2.bitwise_and(img, img, mask = maskb)
        # returns (x,y,w,h) of the rect
        rect = cv2.boundingRect(points) 
        croppedb = resb[rect[1]: rect[1] + rect[3], 
                        rect[0]: rect[0] + rect[2]]

        return resb, croppedb
    
    #----------------------------------------------------------------------
    def overlaying_img(self, img, s_img, x, y):
        "Overlays s_img on img"
        h,w,m = s_img.shape
        img[y:y+h, x:x+w] = s_img
        return img
    
    #----------------------------------------------------------------------
    def adaptive_thresholding(self, img_gray):
        """Performs all possible adaptive thresholding"""
        img = cv.medianBlur(img_gray,5)
        ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
        th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
                                            cv.THRESH_BINARY,11,2)
        th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
                                            cv.THRESH_BINARY,11,2)
        titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
        images = [img, th1, th2, th3]
        for i in range(4):
            plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
            plt.title(titles[i])
            plt.xticks([]),plt.yticks([])
        plt.show()
    #----------------------------------------------------------------------
    #                               ~END~
    #----------------------------------------------------------------------