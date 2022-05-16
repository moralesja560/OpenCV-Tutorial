#face detection
import cv2
import os
#create the absolute paths for external resources
face_cascade_file = os.path.join(os.path.dirname(__file__), 'resources/haarcascade_frontalface_default.xml')
family_file   = os.path.join(os.path.dirname(__file__), 'resources/family.jpg')




faceCascade = cv2.CascadeClassifier(face_cascade_file)

def showInMovedWindow(winname, img, x, y):
    cv2.namedWindow(winname)        # Create a named window
    cv2.moveWindow(winname, x, y)   # Move it to (x,y)
    cv2.imshow(winname,img)

img = cv2.imread(family_file)
imGrayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces =faceCascade.detectMultiScale(imGrayscale,1.3,3)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)


showInMovedWindow('named_window4',img, 0, 400)
cv2.waitKey(0)