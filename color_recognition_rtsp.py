import cv2
from cv2 import imshow
import os
import numpy as np

def empty(a):
	pass

cv2.namedWindow("Trackbars")

cv2.resizeWindow("Trackbars",(640,240))
cv2.createTrackbar("Hue Min","Trackbars",95,179,empty)
cv2.createTrackbar("Hue Max","Trackbars",179,179,empty)
cv2.createTrackbar("Sat Min","Trackbars",21,255,empty)
cv2.createTrackbar("Sat Max","Trackbars",255,255,empty)
cv2.createTrackbar("Val Min","Trackbars",0,255,empty)
cv2.createTrackbar("Val Max","Trackbars",105,255,empty)

RTSP_URL = 'rtsp://root:MubMex30..@10.65.68.29/axis-media/media.amp'
#RTSP_URL = 'rtsp://user:user@10.65.96.119:8554/streaming/channels/0701'
#RTSP_URL ='rtsp://admin:ctrl_es1@10.65.68.125:8554/streaming/channels/0601'


os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'

cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)
#cap.set(cv2.CAP_PROP_BUFFERSIZE, 3)

if not cap.isOpened():
    print('Cannot open RTSP stream')
    exit(-1)
 
while True:
	_, frame1 = cap.read()
	success, frame1 = cap.read()
	#frame for level
	frame = frame1[490:630,200:370]
	#frame = frame1[370:600,600:900]
	#img = cv2.imshow('RTSP stream', frame)
	h_min = cv2.getTrackbarPos("Hue Min","Trackbars")
	h_max = cv2.getTrackbarPos("Hue Max","Trackbars")
	s_min = cv2.getTrackbarPos("Sat Min","Trackbars")
	s_max = cv2.getTrackbarPos("Sat Max","Trackbars")
	val_min = cv2.getTrackbarPos("Val Min","Trackbars")
	val_max = cv2.getTrackbarPos("Val Max","Trackbars")
	imgHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	lower = np.array([h_min,s_min,val_min])
	upper = np.array([h_max,s_max,val_max])
	mask = cv2.inRange(imgHSV,lower,upper)
	imgResult = cv2.bitwise_and(frame,frame, mask=mask)
	#cv2.imshow('mask', mask)
	cv2.imshow('imgResult', mask)
	#cv2.imshow('orig frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		cap.release()
		cv2.destroyAllWindows()
		break
