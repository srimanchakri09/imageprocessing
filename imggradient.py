import cv2
import numpy as np
from matplotlib import pyplot as pyp
img=cv2.imread('messi5.jpg',0)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
lap=cv2.Laplacian(img,cv2.CV_64F,ksize=1)#it takes source data type which is float , ksize is optional
lap=np.uint8(np.absolute(lap))# we need to convert the image into uint from float
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0)#it takes source ,dtype,order of differentiation along x,y since 3rd arug is 1 and 4th is 0 it along x axis
sobely=cv2.Sobel(img,cv2.CV_64F,0,1)
sobelx=np.uint8(np.absolute(sobelx))
sobely=np.uint8(np.absolute(sobely))
combinesobel=cv2.bitwise_or(sobelx,sobely)#bit wise or is used to combine the sobelx and sobely
titles=['original','laplacian','sobledx','sobledy','combined']
images=[img,lap,sobelx,sobely,combinesobel]
for i in range(5):
    pyp.subplot(2,3,i+1)
    pyp.title(titles[i])
    pyp.imshow(images[i])
    pyp.xticks([])
    pyp.yticks([])
pyp.show()
