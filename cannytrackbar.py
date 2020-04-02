import cv2
import numpy as np
from matplotlib import pyplot as pyp
def empty(x):
    pass
#img=cv2.imread('opencv-logo.png',0)
cv2.namedWindow('image')
cv2.createTrackbar('TH1','image',0,300,empty)
cv2.createTrackbar('TH2','image',0,100,empty)
while True:
    img=cv2.imread('opencv-logo.png',0)
    th1=cv2.getTrackbarPos('Th1','image')
    th2=cv2.getTrackbarPos('TH2','image')
    canny=cv2.Canny(img,th1,th2)
    cv2.imshow('image',img)
    if cv2.waitKey==27:
        break
cv2.destroyAllWindows()
