import cv2
import numpy as np
from matplotlib import pyplot as pyp
img=cv2.imread('opencv-logo.png',0)
_,mask=cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)#converting image as threshold binary inverse of the gray scale img since morphological trans sre done in binary image
kernal=np.ones((2,2),np.uint8)#creating a kernal i.e. a shape of the numpy array it can be ones or zeros ie. white or black respectively
#kernal is the thing through which morphological oprations are performed it is a structural image
dilation=cv2.dilate(img,kernal,iterations=2)#dilation removes the other binary value of the kernal and replaces it with the kernal value here the kernal value is
# one i.e. high so it removes the black spots on the images and replace it with the white ones of 2*2 square and if we increase the iterattions ther there will
# be more amount of white which leads to change in the outfit the image particles to avoid that we have erosion which removes the extra outer layer of the image
#by comparing with the original image , the kernal slides over the image and if the value is nit true with the comparsion of the origina one it will erode just
# like soil erosion removing extra layer in the mask image
erosion=cv2.erode(img,kernal,iterations=2)
opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernal)#in this first erosion and then dilation is performed
closing=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernal)#in this first dilation and then erosion is perfomed
mg=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernal)#in this subtraction of dilation and erosion takes place first dilation and erosion takes place and subtraction
th=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernal)#in this subtraction of opened from original image takes place

images=[img,mask,dilation,erosion,opening,closing,mg,th]
titles=['original','binary inv','dilated','eroded','opened','closed','morphgrad','top hat']
for i in range(8):
    pyp.subplot(2,4,i+1)
    pyp.title(titles[i])
    pyp.imshow(images[i],'gray')
    pyp.xticks([])
    pyp.yticks([])

pyp.show()
