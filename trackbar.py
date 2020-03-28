import cv2
import numpy as np
def demo(x):
    #print(x)
    pass
#img=np.zeros((300,512,3),np.uint8)
img = cv2.imread("nature.jpg")
cv2.namedWindow('image')
cv2.createTrackbar('cp','image',0,255,demo)
cv2.createTrackbar('B','image',0,255,demo)
cv2.createTrackbar('G','image',0,255,demo)
cv2.createTrackbar('R','image',0,255,demo)
switch='color/gray'
cv2.createTrackbar(switch,'image',0,1,demo)

while (1):
    img=cv2.imread('nature.jpg')
    #cv2.imshow('image',img)
    if cv2.waitKey(1)==27:
        break
    font = cv2.FONT_ITALIC
    pos=cv2.getTrackbarPos('cp','image')
    cv2.putText(img,str(pos),(50,100),font,4,(255,255,255),2)
    b=cv2.getTrackbarPos("B",'image')
    g=cv2.getTrackbarPos('G','image')
    r=cv2.getTrackbarPos('R','image')
    s=cv2.getTrackbarPos(switch,'image')
    if s==1:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #img[:]=[b,g,r]

    cv2.imshow('image',img)
cv2.destroyAllWindows()
