import cv2
facecascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#it is the xml file which has predifined code for trainers and detectors cascade classifier is the method to callsify what we need
eyecascade=cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
#it is the file for eye classifiaction in github opencv
#img=cv2.imread('messi5.jpg')
cap=cv2.VideoCapture(0)#capturing the video from  default cam
while True:
    ret,img=cap.read()#reading each frame
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#we need to convert into gray for
    faces=facecascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)#facecascade object is used as multiscaledetector it takes three arguments source image
    #scale factor it means it specifies how much the image is reduced at each image scale next is minneighbor it specifies hiw many neighbor each candidate rectangle
    #has to be retain it it gives 4 output values for drawing the rectangle
    print(faces)
    for (x,y,w,h) in faces:#we need to iterate the faces bcpz ther might be many faces in  the image
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)#drawing the rectangle on the faces
        roigray=gray[y:y+h,x:x+w]#creating region of intrest of face since eyes are in the face roi of gray for cascadin the eyes
        roicolor=img[y:y+h,x:x+w]#roi of color is for drawing the rectangles
        eyes=eyecascade.detectMultiScale(roigray)#the other two arguments are not mandatory it also gives the four arguments
        print(eyes)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roicolor,(ex,ey),(ex+w,ey+eh),(0,255,0),2)#creating rectangle on the eyes
    cv2.imshow('image',img)
    if cv2.waitKey(1)==27:
        break
cap.release()
cv2.destroyAllWindows()
