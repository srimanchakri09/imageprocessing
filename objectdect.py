import cv2
import numpy as np
cap=cv2.VideoCapture('vtest.avi')# capturing the existing video
ret,frame1=cap.read()#reading two frames
ret,frame2=cap.read()
while True:
    diff =cv2.absdiff(frame1,frame2)#finding the difference between the two frames
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)#covert the colour since we are going to find contours
    blur=cv2.GaussianBlur(gray,(5,5),0)#filtering the image using guassian blur
    _,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)#finding threshold so that objects can be detected from the background
    dilate=cv2.dilate(thresh,None,iterations=3)#dilating th image used to get better the countours
    contours,_=cv2.findContours(dilate,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)#finding contours on the image
    for contour in contours:
        (x,y,w,h)=cv2.boundingRect(contour)
        #making contour in the shaoe of rectangle since we will get in form of the object and this function gives the x,y
        #co ordinates and width ,height of rectangle
        #area=cv2.contourArea(contour)#finding the area og=f the rectangle so that we can mark specified object only
        if cv2.contourArea(contour)<800:
            continue#if the area of rectangle is lss than 200 it skips the iteration
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)#if area is greater then 200 it draws a rectangle to that contours
        cv2.putText(frame1,'status:()'.format('movement'),(10,20),cv2.FONT_ITALIC,1,(255,0,0),1)
        cv2.imshow('frame',frame1)
        frame1 = frame2  # assinging frame1 into frame2 for the next iteration
        ret,frame2=cap.read()#reading the frame2 for the next iteration
        if cv2.waitKey(100)==27:
            break

cv2.destroyAllWindows()
cap.release()
