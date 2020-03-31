import cv2
import numpy as np
def empty(x):
    pass
img = cv2.imread('messi5.jpg')
cv2.namedWindow('track')
cv2.createTrackbar('LH','track',0,255,empty)
cv2.createTrackbar('LS','track',0,255,empty)
cv2.createTrackbar('LV','track',0,255,empty)
cv2.createTrackbar('UH','track',0,255,empty)
cv2.createTrackbar('US','track',0,255,empty)
cv2.createTrackbar('UV','track',0,255,empty)

while True:
    img=cv2.imread('messi5.jpg')
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lh = cv2.getTrackbarPos('LH', 'track')
    ls = cv2.getTrackbarPos('LS', 'track')
    lv = cv2.getTrackbarPos('LV', 'track')

    uh = cv2.getTrackbarPos('UH', 'track')
    us = cv2.getTrackbarPos('US', 'track')
    uv = cv2.getTrackbarPos('UV', 'track')

    lb=np.array([lh,ls,lv])
    ub=np.array([uh,us,uv])

    mask=cv2.inRange(hsv,lb,ub)
    res=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow('image',img)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
