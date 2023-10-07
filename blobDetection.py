#https://github.com/bnsreenu/python_for_image_processing_APEER/blob/master/tutorial56_simple_blob_detector.py

#Video Playlist: https://www.youtube.com/playlist?list=PLHae9ggVvqPgyRQQOtENr6hK0m1UquGaG

"""
https://www.learnopencv.com/blob-detection-using-opencv-python-c/
BLOB stands for Binary Large OBject and refers to a group of connected pixels in a binary image.
A Blob is a group of connected pixels in an image that share some common
property ( E.g grayscale value ). In the image above, the dark connected regions are blobs, 
and the goal of blob detection is to identify and mark these regions.
How it works:
    1. Threshold input images to binary.
    2. Grouping: connected white/black pixels are grouped together. 
    3. Merging: blobs located closer than minDistBetweenBlobs are merged.
    4. Center & Radius Calculation :  The centers and radii of the new merged blobs are computed and returned.
    
Can be filtered by color, size or shape
"""

import matplotlib.pyplot as plt
import numpy as np
import cv2

# The input image.
image = cv2.imread("images/cast_iron1.tif", 0)
#image = cv2.imread("images/Osteosarcoma_01_small.tif")
#Extract only blue channel as DAPI / nuclear (blue) staining is the best
#channel to perform cell count.
#image=image[:,:,0] 

#No need to pre-threshold as blob detector has build in threshold.
#We can supply a pre-thresholded image.

# Set up the SimpleBlobdetector with default parameters.
params = cv2.SimpleBlobDetector_Params()

# Filter by minDistBetweenBlobs
# Works if there are several thresholds only
#SimpleBlobDetector has many parameters, and the two are minDistBetweenBlobs 
# and threshold (set by minThreshold, maxThreshold, thresholdStep)
# A developer is forced to use more than one threshold values to use 
# minDistBetweenBlobs parameter, which could degrade processing speed. 
# It also confuses beginners without knowledge in the interworkings of the 
# code because one would normally use just one threshold for blob detection.
# minDistBetweenBlobs only works with more than one threshold because the code 
# that uses them can never be reached.
params.minDistBetweenBlobs = 0

# Define thresholds
#Can define thresholdStep. See documentation. 
params.minThreshold = 0
params.maxThreshold = 255

# Filter By Repeatability
# Finds blob centers at d/t thresholds; the minimum valid value is 1
params.minRepeatability = 1

# Filter by Area.
# Extract blobs that have an area between minArea (inclusive) and maxArea (exclusive).
params.filterByArea = True
params.minArea = 50
params.maxArea = 10000

# Filter by Color (black=0, white=255)
#  This filter compares the intensity of a binary image at the center of a blob to blobColor. 
#  If they differ, the blob is filtered out. Use blobColor = 0 to extract dark blobs and 
# blobColor = 255 to extract light blobs.
params.filterByColor = False  #Set true for cast_iron as we'll be detecting black regions
params.blobColor = 0

# Filter by Circularity
# Extracted blobs have circularity ( 4∗π∗Areaper/(imeter∗perimeter)) between minCircularity 
# (inclusive) and maxCircularity (exclusive).
params.filterByCircularity = True
params.minCircularity = 0.5
params.maxCircularity = 1

# Filter by Convexity
# Extracted blobs have convexity (area / area of blob convex hull) between minConvexity
# (inclusive) and maxConvexity (exclusive).
params.filterByConvexity = True
params.minConvexity = 0.5
params.maxConvexity = 1

# Filter by InertiaRatio
#  Extracted blobs have this ratio between minInertiaRatio (inclusive) and 
#  maxInertiaRatio (exclusive).
params.filterByInertia = True
params.minInertiaRatio = 0
params.maxInertiaRatio = 1

# Setup the detector with parameters
detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs
keypoints = detector.detect(image)

print("Number of blobs detected are : ", len(keypoints))


# Draw blobs
img_with_blobs = cv2.drawKeypoints(image, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
plt.imshow(img_with_blobs)
cv2.imshow("Keypoints", img_with_blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save result

"""
params = struct();
params.ThresholdStep = 10;
params.MinThreshold = 10;
params.MaxThreshold = 220;

params.MinRepeatability = 2;

params.MinDistBetweenBlobs = 10;

params.FilterByColor = false;
params.BlobColor = 0;

params.FilterByArea = false;
params.MinArea = 25;
params.MaxArea = 5000;

params.FilterByCircularity = false;
params.MinCircularity = 0.9;
params.MaxCircularity = 1e37;

params.FilterByInertia = false;
params.MinInertiaRatio = 0.1;
params.MaxInertiaRatio = 1e37;

params.FilterByConvexity = false;
params.MinConvexity = 0.95;
params.MaxConvexity = 1e37;
"""
