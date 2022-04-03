#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 05:33:22 2019

@author: alem
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 04:54:19 2019

@author: alem

https://docs.opencv.org/3.1.0/dd/d49/tutorial_py_contour_features.html
"""

import cv2
import numpy as np
img = cv2.imread('fig_6.jpg',0)
cv2.imshow('Orig', img)
ret,thresh = cv2.threshold(img,127,255,0)
contours,hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]
#1. Moments
M = cv2.moments(cnt)
print(M)

#Centroid
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

#2. Contour Area
area = cv2.contourArea(cnt)

#3. Contour Perimeter
perimeter = cv2.arcLength(cnt,True)


#4. Contour Approximation
epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)


#5. Convex Hull
#hull = cv2.convexHull(points[, hull[, clockwise[, returnPoints]])
hull = cv2.convexHull(cnt)
#6. Checking Convexity


k = cv2.isContourConvex(cnt)

#7. Bounding Rectangle

x,y,w,h = cv2.boundingRect(cnt)
cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
#7.b. Rotated Rectangle
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.drawContours(img,[box],0,(0,0,255),2)
cv2.imshow('Boxed', img)
#Both the rectangles are shown in a single image. Green rectangle shows the 
#normal bounding rect. Red rectangle is the rotated rect.
#8. Minimum Enclosing Circle
(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
cv2.circle(img,center,radius,(0,255,0),2)

#9. Fitting an Ellipse
#ellipse = cv2.fitEllipse(cnt)
#cv2.ellipse(img,ellipse,(0,255,0),2)

#10. Fitting a Line
rows,cols = img.shape[:2]
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)
cv2.waitKey(0)
cv2.destroyAllWindows()