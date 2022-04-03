import cv2


rgb_color=(0, 0, 0)
color = tuple(reversed(rgb_color))
image = np.zeros((width,height, 3), np.uint8)
color = tuple(reversed(rgb_color))
image[:] = color

# Image to be encrypted
imgTobeEnc = cv2.imread("wallFacesWinsdnd.jpg")
height, width = imgTobeEnc.shape[:2]
l_img=cv2.resize(image,(width,height))



key = cv2.imread("wallFacesWinsdnd.jpg")


cv2.rectangle(img22,(62,250),(93,283),(255,0,0),3) 
cv2.rectangle(img22,(129,232),(168,277),(255,0,0),3) 
cv2.rectangle(img22,(7,108),(211,222),(255,0,0),3) 
cv2.rectangle(img22,(288,106),(421,239),(255,0,0),3) 
cv2.imwrite('wallFacesWinsdnd2.jpg',img22)   


s_img = mask[y:y+h, x:x+w]
l_img[y:y+h, x:x+w] = s_img       
b = np.asarray(l_img)
 a = np.asarray(img)
