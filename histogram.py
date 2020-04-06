import cv2
import numpy as np
from matplotlib import pyplot as pyp
#img1=np.zeros((500,500),np.uint8)# creating numpy black image
img=cv2.imread('messi5.jpg')
#b,g,r=cv2.split(img)
cv2.imshow('image',img)
#cv2.imshow('b',b)
#cv2.imshow('g',g)
#cv2.imshow('r',r)
hist=cv2.calcHist([img],[0],None,[256],[0,256])
pyp.plot(hist)
#pyp.hist(b.ravel(),256,[0,256])
#pyp.hist(g.ravel(),256,[0,256])
#pyp.hist(r.ravel(),256,[0,256])
#pyp.hist(img1.ravel(),256,[0,256])
pyp.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
