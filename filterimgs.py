import cv2
import numpy as np
from matplotlib import pyplot as pyp
img=cv2.imread('opencv-logo.png')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
kernel=np.ones((5,5),np.float32)/25#define a kenel of ones and divide it with product kernel width and height it is fir homogenous filter only
hfil=cv2.filter2D(img,-1,kernel)#it takes source ddepth and kernel and convolve image with the source add kernel ad=nd source and divides with 25
avgfil=cv2.blur(img,(5,5))#avg filter takes the avg value value of the neughbouring values where the kernel placed in the image
gausfil=cv2.GaussianBlur(img,(5,5),5,5)#it takes kernek size and std deviation along x,y direction of the kernel
medianfil=cv2.medianBlur(img,5)#it takes source and kernel size it givs the medain pixel vallue and that will be placed below the kernel
bilfil=cv2.bilateralFilter(img,5,0,0)# it is the best filter which also filters the edges
titles=['oriimg','homogenised','averaged','gaussined','median filter','bilateral fil']
images=[img,hfil,avgfil,gausfil,medianfil,bilfil]
for i in range(6):
    pyp.subplot(2,3,i+1)
    pyp.title(titles[i])
    pyp.imshow(images[i])
    pyp.xticks([])
    pyp.yticks([])
pyp.show()
