#resizing and cropping
import cv2
import numpy as np

img = cv2.imread("resources/unresize.jpg")

#this is a list of possible image sizes based on % and width/height ratio
print(f"ratio of image is {img.shape[1]/img.shape[0]}, so multiply height for this coefficient")
print(f"50% would be {img.shape[0]/2} and width would be {img.shape[1]/2}")

imgResize = cv2.resize(img,(450,1000))

#cropping
imgCropped = imgResize[100:500,100:300]


cv2.imshow("Image",imgResize)
cv2.imshow("Image", imgCropped)
cv2.waitKey(0)