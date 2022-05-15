import cv2
from cv2 import imshow
import os
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

RTSP_URL = 'rtsp://root:MubMex30..@10.65.68.48/axis-media/media.amp'
#RTSP_URL = 'rtsp://user:user@10.65.96.119:8554/streaming/channels/0701'
#RTSP_URL ='rtsp://admin:ctrl_es1@10.65.68.125:8554/streaming/channels/0101'##


os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'
 
cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)

if not cap.isOpened():
    print('Cannot open RTSP stream')
    exit(-1)
 
while True:
	_, frame = cap.read()
	#img = cv2.imshow('RTSP stream', frame)
	h_min = cv2.getTrackbarPos("Hue Min","Trackbars")
	h_max = cv2.getTrackbarPos("Hue Max","Trackbars")
	s_min = cv2.getTrackbarPos("Sat Min","Trackbars")
	s_max = cv2.getTrackbarPos("Sat Max","Trackbars")
	val_min = cv2.getTrackbarPos("Val Min","Trackbars")
	val_max = cv2.getTrackbarPos("Val Max","Trackbars")
	lower = np.array([h_min,s_min,val_min])
	upper = np.array([h_max,s_max,val_max])
	mask = cv2.inRange(frame,lower,upper)
	imgResult = cv2.bitwise_and(frame,frame, mask=mask)
	cv2.imshow('RTSP streams', mask)
	cv2.imshow('RTSP stream2', imgResult)
	cv2.waitKey(1)


cap.release()
cv2.destroyAllWindows()