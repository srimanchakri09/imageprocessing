import cv2
import numpy as np
img=cv2.imread('shapes.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#conbverting into gray as we find contours
_,thresh=cv2.threshold(gray,10,255,cv2.THRESH_BINARY_INV)#finding threshold to find contours
contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
for contour in contours:#iterating among the contours to find the shape of each of contour
    app=cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)#this function is used to get the polygon and it takes four arguments
    cv2.drawContours(img,[app],0,(0,0,0),3)
    x=app.ravel()[0]#finding the x co-ordinate raavel is like function app is a varialble\
    y=app.ravel()[1]# finding the y co-ordinate and making it ti=o move above by 5 usnits
    if len(app)==3:#as app gives the poloygon we can calculate its length and find shapes
        cv2.putText(img,'triangle',(x,y),cv2.FONT_ITALIC,3,(0,0,0),3)
    elif len(app)==4:# if it is 4 we can have rectangle and square so we can find is by using bounding.Rect method which gives four outputs x,y co-ordinate
        (x1,y1,w,h)=cv2.boundingRect(app)# width , height and by finding the ratio between width and height we can judge either it is a squre or rect
        ratio=float(x)/y
        if ratio>=0.95 and ratio<=1.05:
            cv2.putText(img, 'square', (x, y), cv2.FONT_ITALIC, 3, (0, 0, 0), 3)
        else:
            cv2.putText(img, 'rectangle', (x, y), cv2.FONT_ITALIC, 3, (0, 0, 0), 3)
    elif len(app)==5:
        cv2.putText(img, 'pentagon', (x, y), cv2.FONT_ITALIC, 3, (0, 0, 0), 3)
    elif len(app)==6:
        cv2.putText(img, 'hexagon', (x, y), cv2.FONT_ITALIC, 3, (0, 0, 0), 3)
    elif len(app)==7:
        cv2.putText(img, 'heptagon', (x, y), cv2.FONT_ITALIC, 3, (0, 0, 0), 3)
    elif len(app)==8:
        cv2.putText(img, 'octagon', (x, y), cv2.FONT_ITALIC, 3, (0, 0, 0), 3)
    else:
        cv2.putText(img, 'circle', (x, y), cv2.FONT_ITALIC, 3, (0, 0, 0), 3)
cv2.imshow('shapes',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
