import cv2
import numpy as np
def empty(x):                                  #defining def as to pass (simply)
    pass
img = cv2.imread('messi5.jpg')#reading an image
cv2.namedWindow('track')#naming the window which will be used in trackbar function 
cv2.createTrackbar('LH','track',0,255,empty)#creating trackbars as lower hue  since hsv scale has 6 parameters[lowe,upper hue,staturation,value]
cv2.createTrackbar('LS','track',0,255,empty)#creating lowe staturation
cv2.createTrackbar('LV','track',0,255,empty)#creating lower value
cv2.createTrackbar('UH','track',0,255,empty)#creating upper hue
cv2.createTrackbar('US','track',0,255,empty)#creating upper staturation
cv2.createTrackbar('UV','track',0,255,empty)#creating upper value
#runig while loop to excute each and every sec change done by us while chamging track bars value
while True:
    img=cv2.imread('messi5.jpg')#reading image each nd every time its not require iw=f we create image using numpy aray
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)#the main step is to cinver bgr image into hsv image since the image is to be read in hsv scale for object detectjon
    lh = cv2.getTrackbarPos('LH', 'track')#getting trackbarpos
    ls = cv2.getTrackbarPos('LS', 'track')
    lv = cv2.getTrackbarPos('LV', 'track')

    uh = cv2.getTrackbarPos('UH', 'track')
    us = cv2.getTrackbarPos('US', 'track')
    uv = cv2.getTrackbarPos('UV', 'track')

    lb=np.array([lh,ls,lv])# creating array of all lower values
    ub=np.array([uh,us,uv])#creating array of all upper values
# any color ranges in these lower and upper values so we can detect colour  and create a xerox like image of the needed colour i.e mask 
    mask=cv2.inRange(hsv,lb,ub)#mask image is created in the range of lb,up of the hsv image 
    res=cv2.bitwise_and(img,img,mask=mask)# bitwise operation is done betwwen mask and source image here if we dont give mask keyword it gives the source 
    # image result so we need to specify it as mask image
    cv2.imshow('image',img)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    if cv2.waitKey(1)==27:#the main important in trackbars is delay it should be 1 not 0 since we can able to change the image each and every time if it is 0 
        break             # then there is no delay and even though if we change colour there is no change in image 
cv2.destroyAllWindows()
