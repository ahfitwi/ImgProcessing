#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 23:19:30 2019

@author: alem
"""

import cv2
import numpy as np
fn = 'fig_4.jpg'
im_gray = cv2.imread(fn, cv2.CV_LOAD_IMAGE_GRAYSCALE)
im_gray_mat = cv2.fromarray(im_gray)
im_bw = cv2.CreateImage(cv2.GetSize(im_gray_mat), cv2.IPL_DEPTH_8U, 1);
im_bw_mat = cv2.GetMat(im_bw)
threshold = 0 # 128#255# HAS NO EFFECT!?!?
cv2.Threshold(im_gray_mat, im_bw_mat, threshold, 255, cv2.CV_THRESH_BINARY | cv2.CV_THRESH_OTSU);
cv2.imshow('', np.asarray(im_bw_mat))
cv2.waitKey()