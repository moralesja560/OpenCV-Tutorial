# import the opencv librarysadasdasd
from fileinput import filename
import cv2
import os


#resources
file_name = os.path.join(os.path.dirname(__file__), 'resources/haarcascade_frontalface_default.xml')

faceCascade = cv2.CascadeClassifier(file_name)
# define a video capture object
vid = cv2.VideoCapture(0)
  
while(True):
      
    # Capture the video frame
    # by frame
    ret, img = vid.read()  
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    faces = faceCascade.detectMultiScale(gray_img, 1.25, 4) 
    for (x,y,w,h) in faces: 
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)  
        rec_gray = gray_img[y:y+h, x:x+w] 
        rec_color = img[y:y+h, x:x+w] 
    cv2.imshow('Face Recognition',img) 
   
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()