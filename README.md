# ImgProcessing
Micellaneous Image Processing Methods and Techniques.
- **Errode**: An erosion eats away at the foreground pixels thereby decreasing the size of the foreground object.
  - img = cv2.erode(img, np.ones([3,3], np.uint8), iterations = 3)
- **Dilate**: The opposite of an erosion is a dilation. A dilation grows the foreground pixels thereby increasing the size of foreground objects
    - Especially useful for joining broken parts of an image together
    - img = cv2.dilate(img, np.ones([3, 3], np.uint8), iterations= 3)
- **Distortion**: https://www.edmundoptics.com/knowledge-center/application-notes/imaging/distortion/
