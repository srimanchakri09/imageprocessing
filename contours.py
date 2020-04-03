import cv2
import numpy as np
img=cv2.imread('opencv-logo.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#for finding contours we should convert it into gray scale img
res,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)#contor can be done if the image is appiled to threshold or canny edge detection
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)#we can get contours by this function
print('no.of countours'+str(len(contours)))
print(contours[0])
cv2.drawContours(img,contours,-1,(0,255,0),3)#it draws the line on the contour co ordinates which are in the form numoy array in the contour variable
cv2.imshow('image',img)
#cv2.imshow('grayed',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
