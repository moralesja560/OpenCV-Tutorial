import cv2
from cv2 import imshow
import os

RTSP_URL = 'rtsp://root:MubMex30..@10.65.68.9/axis-media/media.amp'
 
os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'
 
cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)

if not cap.isOpened():
    print('Cannot open RTSP stream')
    exit(-1)
 
while True:
    _, frame = cap.read()
    cv2.imshow('RTSP stream', frame)
 
    if cv2.waitKey(1) == 27: #escape key
        break
 
cap.release()
cv2.destroyAllWindows()