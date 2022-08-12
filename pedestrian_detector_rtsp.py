#import the necessary utilities
from imutils.object_detection import non_max_suppression
#Non max suppresion, a part of imutils package, is the algorithm that groups the overlapping bounding boxes into a big box
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
import os

#construct the argument parse
#this stuff handle parsing our command line arguments. We require the image directory path.
#ap = argparse.ArgumentParser()
#ap.add_argument("-i","--images",required=True,help="path to images directory")
#args = vars(ap.parse_args())

def empty(a):
	pass

frameWidth = 640
frameHeight = 480

#cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
#RTSP_URL ='rtsp://admin:ctrl_es1@10.65.68.125:8554/streaming/channels/0601'
RTSP_URL = 'rtsp://user:user@10.65.96.119:8554/streaming/channels/1601'
 
os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'
cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 3)

#initialize the HOG descriptor / person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

#at this point, we have loaded a pretrained OpenCV pedestrian detector. From now on its just a matter of loading and processing some image.

cv2.namedWindow("Trackbars")

cv2.resizeWindow("Trackbars",(640,240))
cv2.createTrackbar("Winstride","Trackbars",1,6,empty)
cv2.createTrackbar("Scale","Trackbars",10,150,empty)


while True:
	success, imagePath = cap.read()
	#load the image and resize it
	#image = cv2.imread(imagePath)
	image = imagePath
	image = imutils.resize(image,width=min(400, image.shape[1]))
	orig = image.copy()
	w_stride = cv2.getTrackbarPos("Winstride","Trackbars")
	track_scale = cv2.getTrackbarPos("Scale","Trackbars")
	track_scale = track_scale/100
	#try to detect people on the image
	(rects,weights) = hog.detectMultiScale(image,winStride=(w_stride,w_stride),padding=(8,8), scale=track_scale)

	#WinStride parameter: Imagine a field (a picture) that has a width of 1920 px and a height of 1080px. 
		#we scan that field using a window that is 1 px wide and 1 px high. That leaves us with 2.1 million images to be scanned.
		# When using pedestrian detection, we must adjust this parameters to avoid wasteful image processing
	



	#apply non-maxima suppression to the bounding boxes using a fairly large overlap threshold
	rects = np.array([[x,y,x+w,y+h] for (x,y,w,h) in rects])
	pick = non_max_suppression(rects, probs=None, overlapThresh=0.6)

	#draw the final bounding boxes
	for (xA,yA,xB,yB) in pick:
		cv2.rectangle(image,(xA,yA),(xB,yB),(0,255,0),2)
	
	#show some information on the number of bounding boxes
	#filename = imagePath[imagePath.rfind("/")+1:]
	#print("[INFO] {}: {} original boxes, {} after suppression".format(filename, len(rects), len(pick)))

	#show the output images
	#cv2.imshow("Before NMS",orig)
	cv2.imshow("AfterNMS",image)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
