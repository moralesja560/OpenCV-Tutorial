#face detection
import cv2

faceCascade = cv2.CascadeClassifier("resources/haarcascade_frontalface_default.xml")

def showInMovedWindow(winname, img, x, y):
    cv2.namedWindow(winname)        # Create a named window
    cv2.moveWindow(winname, x, y)   # Move it to (x,y)
    cv2.imshow(winname,img)

img = cv2.imread('resources/family.jpg')
imGrayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces =faceCascade.detectMultiScale(imGrayscale,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)


showInMovedWindow('named_window4',img, 0, 400)
cv2.waitKey(0)