import cv2
import numpy as np
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)

myColors = [[0,83,0,179,163,28],
			[2,148,18,126,254,255],
			[1,36,146,60,255,255]]



def findColor(img,myColors):
	imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	for color in myColors:
		lower = np.array(color[0:3])
		upper = np.array(color[3:6])
		mask = cv2.inRange(imgHSV,lower,upper)
		cv2.imshow(str(color[1]), mask)



while True:
    success, img = cap.read()
    newPoints = findColor(img, myColors)


    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break