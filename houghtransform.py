import cv2
import numpy as np
img=cv2.imread('sudoku.png')
cv2.imshow('original',img)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#convert clor to gray to find canny edge detecion
edge=cv2.Canny(gray,50,150)
cv2.imshow('cannied',edge)
lines=cv2.HoughLinesP(edge,1,np.pi/180,100,minLineLength=100,maxLineGap=10)#it takes 6 arguments source and next is rho value which is distance resolution accumulator that
# it is the distance of the point from the origin it is normally denoted as '1' and third one  is theta it is the angle resolution accumulator means it gives
#the angle thriugh which the line should be rotated  and fourth is threshold value the lines which are above this value are printed next one is minlinelength
#lines less than this value are neglected so that we can get some part of the line and last os the maxlinegap between two lines
print(lines)#output will be the matrix array of 4 values in each they are the x,y coordinates of the lines that means in each line two coordinates are gives
for line in lines:
    x1,y1,x2,y2= line[0]#since it has 4 values andthis is the advantage of the houghtransofrmp that is we need not to find the other lines
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
