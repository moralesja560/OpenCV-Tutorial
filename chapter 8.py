import cv2
from cv2 import COLOR_BGR2GRAY
from cv2 import Canny
import numpy as np

def showInMovedWindow(winname, img, x, y):
    cv2.namedWindow(winname)        # Create a named window
    cv2.moveWindow(winname, x, y)   # Move it to (x,y)
    cv2.imshow(winname,img)

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        
        #give a threshold to avoid any noise
        if area>429:
            print(area)
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
            #approximate the corners
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print (len(approx))




path = 'resources/circles.jpg'
img = cv2.imread(path)
imgContour = img.copy()

#convert into grayscale
imGrayscale = cv2.cvtColor(img,COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img,(7,7),1)
imgCanny = cv2.Canny(img,50,50)
imgBlank = np.zeros_like(img)
getContours(imgCanny)

#original
#showInMovedWindow('named_window',img, 0, 400)
#grayscale
#showInMovedWindow('named_window2',imGrayscale, 0, 400)
#blur
#showInMovedWindow('named_window3',imgBlur, 0, 400)
#canny
#showInMovedWindow('named_window3',imgCanny, 0, 400)
#Blank
showInMovedWindow('named_window4',imgContour, 0, 400)
#



cv2.waitKey(0)
