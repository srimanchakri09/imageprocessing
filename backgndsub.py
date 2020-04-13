import cv2
import numpy as np
cap=cv2.VideoCapture('vtest.avi')
#fgbg=cv2.bgsegm.createBackgroundSubtractorMOG()#we are creating a object bgsegm to the createBackgroundSubtractorMOG method this method is a guassian mixture based
#fore ground and background subtraction algorithm and it takes no arguments since all are given default but we can make changes  
#IT IS GIVING THE ERROR AS BGSEGM IS NOT FIND IN THE CV2. CLASS
#fgbg=cv2.createBackgroundSubtractorMOG2(detectShadows=False)#it is the another backgrounf=d sun=btraction method which doesnt require any object and works same as above method
#but it gives shadows of the moving objects so we can change the detectshadows argument by making it false but by original it is true
fgbg=cv2.createBackgroundSubtractorKNN(detectShadows=False)# it is similar to createBackgroundsubtractorMOG2 method butt gives better result
while True:
    ret,frame=cap.read()
    fgmask=fgbg.apply(frame)#by using fgbg as an object and apply function we are going to apply the above defined methods to frame to detect the moving objects
    #in the video captured by the static camera
    cv2.imshow("frame",frame)
    cv2.imshow("masked frame",fgmask)
    if cv2.waitKey(1)==27:
        break
cap.release()
cv2.destroyAllWindows()
