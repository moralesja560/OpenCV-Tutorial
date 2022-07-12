import cv2
import os
import sys
from datetime import datetime
import time

# Getting the current date and time
dt = datetime.now()

# getting the timestamp
ts = datetime.timestamp(dt)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

RTSP_URL = 'rtsp://user:user@10.65.96.76:8554/streaming/channels/1401'
 
os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'
 
cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)

if not cap.isOpened():
    print('Cannot open RTSP stream')
    exit(-1)
 
while True:
	_, frame1 = cap.read()
	frame = frame1[620:730,700:1300]
	cv2.imshow('RTSP stream', frame)
	dt = datetime.now()
	ts = datetime.timestamp(dt)
	print(resource_path(f'resources/img{ts}.jpg'))
	test = cv2.imwrite(resource_path(f'resources/img{ts}.jpg'), frame)
	print(test)
	time.sleep(600)
	if cv2.waitKey(1) == 27: #escape key
		break
 
cap.release()
cv2.destroyAllWindows()