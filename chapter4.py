import cv2

import numpy as np

img = np.zeros((512,512,3),np.uint8)
#print(img.shape)
#range to color 
#img[50:100,0:100] = 255,0,0
						#width      #height
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)

#draw a rectangle
	#image
	#upper left corner (maximum parameter is image width or height)
	#lower right corner
	#color
	#thickness
cv2.rectangle(img,(0,0),(511,512),(0,0,255),2)

#circle
	#image
	#center
	#radius
	#color
	#thickness
cv2.circle(img, (250,250),30,(255,255,50),5)

#put text
	#target image
	#text
	#where to put it
	#font
	#text scale
	#color
	#thickness
cv2.putText(img,"OPENCV ",(100,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,158,190),2)





cv2.imshow("image", img)

cv2.waitKey(0)


