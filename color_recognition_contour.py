import cv2
import os
import numpy as np

#file_name = os.path.join(os.path.dirname(__file__), 'resources/circles.jpg')
#assert os.path.exists(file_name)

frameWidth = 640
frameHeight = 480

#cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
RTSP_URL ='rtsp://admin:ctrl_es1@10.65.68.125:8554/streaming/channels/0601'
 
os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'
 
cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150)

#blue liquid, yellow ziptie and orange card
#first min values then max values
#myColors = ([[36,61,159,75,255,255],[0,148,18,126,254,255],[1,36,146,60,112,255]])
#myColors = ([[36,61,159,75,255,255]]) # color de etiqueta verde
myColors = ([[108,122,63,121,255,255]])  #azul mubea
#please make the first numbers of each color different.

#hue min , sat min, value min  hue max, sat max, value max.

def getContours(img):
	control_n = 0
	contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
	x,y,w,h = 0,0,0,0
	for cnt in contours:
		area = cv2.contourArea(cnt)
		if area>900:
			control_n +=1
			cv2.drawContours(img_Result, cnt, -1, (0, 0,255), 3)
			peri = cv2.arcLength(cnt,True)
			approx = cv2.approxPolyDP(cnt,0.02*peri,True)
			x, y, w, h = cv2.boundingRect(approx)
	print(control_n)
	return x+w//2,y


def findColor(img,myColors):
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(img,lower,upper) #do not use imgHSV, use normal img.
        getContours(mask)
        #cv2.imshow(str(color[0:6]),mask)
        #cv2.imshow('RTSP stream2', img)


while True:
	success, img = cap.read()
	imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	img_Result = img.copy()
	findColor(imgHSV,myColors)
	cv2.imshow('Contours', img_Result)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
