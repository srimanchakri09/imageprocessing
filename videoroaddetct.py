import cv2
import numpy as np
from matplotlib import pyplot as pyp
def roi(img,vertices):
    mask=np.zeros_like(img)
    channelcount=image.shape[2]
    match_mask_colour=(255,)*channelcount
    cv2.fillPoly(mask,vertices,match_mask_colour)
    masked_image=cv2.bitwise_and(img,mask)
    return masked_image
def drawlines(img,lines):
    img=np.copy(img)
    blankimg=np.zeros((img.shape[0],img.shape[1],3),np.uint8)
    for line in lines:
        for x1,y1,x2,y2 in line:
        #x1,y1,x2,y2=line[0]
            cv2.line(blankimg,(x1,y1),(x2,y2),(0,255,0),3)
    img=cv2.addWeighted(img,0.8,blankimg,1,0.0)
    return img
#image=cv2.imread('road.jpg')
#image =cv2.cvtColor(image,cv2.COLOR_BGR2RGB)#as we r using matplotlib so we need convert into rgb
def process(image):
    print(image.shape)
    height=image.shape[0]# since it gives a tuple of three values height,width and no.of channels
    width=image.shape[1]
    roivertices=[
        (50,height),
        (width/2,height/2+50),
        (width,height)
    ]
    grayimg=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    caniedimg=cv2.Canny(grayimg,200,200)
    cropedimg=roi(caniedimg,np.array([roivertices],np.int32))
    Lines=cv2.HoughLinesP(cropedimg,1,np.pi/180,100,minLineLength=20,maxLineGap=10)
    print(Lines)
    linedimg=drawlines(image,Lines)
    return linedimg
#cv2.imshow("croped",cropedimg)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#pyp.imshow(linedimg)
#pyp.show()
cap=cv2.VideoCapture('test.mp4')
while True:
    ret,frame=cap.read()
    frame1=process(frame)
    cv2.imshow("linedvideo",frame1)
    if cv2.waitKey(1)==27:
        break
cap.release()
cv2.destroyAllWindows()
