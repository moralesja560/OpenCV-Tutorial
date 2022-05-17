import cv2
import os
import numpy as np

#file_name = os.path.join(os.path.dirname(__file__), 'resources/circles.jpg')
#assert os.path.exists(file_name)

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150)

#blue liquid, yellow ziptie and orange card
#first min values then max values
myColors = ([[0,83,2,179,255,69],[0,148,18,126,254,255],[1,36,146,60,112,255]])
#please make the first numbers of each color different.

#hue min , sat min, value min  hue max, sat max, value max.

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>100:
            cv2.drawContours(img_Result, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2,y


def findColor(img,myColors):
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(img,lower,upper) #do not use imgHSV, use normal img.
        getContours(mask)
        cv2.imshow(str(color[0:6]),mask)
        cv2.imshow('RTSP stream2', img)


while True:
    success, img = cap.read()
    img_Result = img.copy()
    findColor(img,myColors)
    cv2.imshow('Contours', img_Result)
	
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
