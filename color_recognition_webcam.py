import cv2
from cv2 import imshow
import os
import numpy as np

def empty(a):
	pass

cv2.namedWindow("Trackbars")

cv2.resizeWindow("Trackbars",(640,240))
cv2.createTrackbar("Hue Min","Trackbars",0,179,empty)
cv2.createTrackbar("Sat Min","Trackbars",83,255,empty)
cv2.createTrackbar("Val Min","Trackbars",0,255,empty)
cv2.createTrackbar("Hue Max","Trackbars",179,179,empty)

cv2.createTrackbar("Sat Max","Trackbars",163,255,empty)

cv2.createTrackbar("Val Max","Trackbars",28,255,empty)

# define a video capture object
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)


if not cap.isOpened():
    print('Cannot open RTSP stream')
    exit(-1)
 
while True:
	_, frame = cap.read()
	#img = cv2.imshow('RTSP stream', frame)
	h_min = cv2.getTrackbarPos("Hue Min","Trackbars")
	s_min = cv2.getTrackbarPos("Sat Min","Trackbars")
	val_min = cv2.getTrackbarPos("Val Min","Trackbars")
	h_max = cv2.getTrackbarPos("Hue Max","Trackbars")
	s_max = cv2.getTrackbarPos("Sat Max","Trackbars")
	val_max = cv2.getTrackbarPos("Val Max","Trackbars")
	lower = np.array([h_min,s_min,val_min])
	upper = np.array([h_max,s_max,val_max])
	mask = cv2.inRange(frame,lower,upper)
	imgResult = cv2.bitwise_and(frame,frame, mask=mask)
	cv2.imshow('RTSP streams', mask)
	cv2.imshow('RTSP stream2', imgResult)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		cap.release()
		cv2.destroyAllWindows()
		break
        


