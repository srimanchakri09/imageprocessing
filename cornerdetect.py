import cv2
import numpy as np
img=cv2.imread('chessboard.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=np.float32(gray)#for horris corner detection image should be in grayscale float32 format only
dst=cv2.cornerHarris(gray,2,3,0.04)#it takes four arguments source bllocksize that means window size next is kernelsize nd last is harris detctor free parameter
dst=cv2.dilate(dst,None)
img[dst>0.018*dst.max()]=[0,255,0]#giving the threshold value for corner detection
cv2.imshow('final',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
