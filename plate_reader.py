import cv2
import os

frameWidth = 800
frameHeight = 600

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.set(4, frameHeight)
cap.set(3,frameWidth)
cap.set(10,150)

plate_cascade_file = os.path.join(os.path.dirname(__file__), 'resources/haarcascade_frontalface_default.xml')
family_file   = os.path.join(os.path.dirname(__file__), 'resources/family.jpg')


def showInMovedWindow(winname, img, x, y):
    cv2.namedWindow(winname)        # Create a named window
    cv2.moveWindow(winname, x, y)   # Move it to (x,y)
    cv2.imshow(winname,img)

faceCascade = cv2.CascadeClassifier(plate_cascade_file)

while True:
	success, img = cap.read()
	imGrayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	numberPlate =faceCascade.detectMultiScale(imGrayscale,1.3,3)
	for (x,y,w,h) in numberPlate:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
