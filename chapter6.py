#color detection
import cv2
import numpy as np
def empty(a):
	pass

cv2.namedWindow("Trackbars")

cv2.resizeWindow("Trackbars",(640,240))
cv2.createTrackbar("Hue Min","Trackbars",0,179,empty)
cv2.createTrackbar("Hue Max","Trackbars",50,179,empty)
cv2.createTrackbar("Sat Min","Trackbars",0,255,empty)
cv2.createTrackbar("Sat Max","Trackbars",51,255,empty)
cv2.createTrackbar("Val Min","Trackbars",90,255,empty)
cv2.createTrackbar("Val Max","Trackbars",255,255,empty)

while True:
	img = cv2.imread("resources/Imagen00012.bmp")
	imgResize = cv2.resize(img,(1366,720))
	imgHSV = cv2.cvtColor(imgResize,cv2.COLOR_BGR2HSV)
	h_min = cv2.getTrackbarPos("Hue Min","Trackbars")
	h_max = cv2.getTrackbarPos("Hue Max","Trackbars")
	s_min = cv2.getTrackbarPos("Sat Min","Trackbars")
	s_max = cv2.getTrackbarPos("Sat Max","Trackbars")
	val_min = cv2.getTrackbarPos("Val Min","Trackbars")
	val_max = cv2.getTrackbarPos("Val Max","Trackbars")
	lower = np.array([h_min,s_min,val_min])
	upper = np.array([h_max,s_max,val_max])
	mask = cv2.inRange(imgResize,lower,upper)
	imgResult = cv2.bitwise_and(imgResize,imgResize,mask=mask)

	cv2.imshow("Original", imgResize)
	cv2.imshow("HSV", imgHSV)
	cv2.imshow("Mask", mask)
	cv2.imshow("MSK", imgResult)
	cv2.waitKey(1)

#coke bottle 0,90,0,37,87,255
#yellow tape 0,102,159,255,0,249

