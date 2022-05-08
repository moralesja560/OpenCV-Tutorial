import cv2
from cv2 import COLOR_BGR2GRAY
import numpy as np

img = cv2.imread("resources/testimg.jpg")
kernel = np.ones((5,5),np.uint8)

#convert into grayscale
imgGray = cv2.cvtColor(img,COLOR_BGR2GRAY)
#blur image
imgGray_blur = cv2.GaussianBlur(imgGray,(9,9),0)
#canny function
imgCanny = cv2.Canny(img,200,150)
#edge thickening
imageDialation = cv2.dilate(imgCanny,kernel,iterations=3)
#edge erosion
image_erosion = cv2.erode(imageDialation,kernel,iterations=2)


cv2.imshow("grayscale", imgGray)
cv2.imshow("blurred", imgGray_blur)
cv2.imshow("canny", imgCanny)
cv2.imshow("Dialation", imageDialation)
cv2.imshow("Erosion", image_erosion)
cv2.waitKey(0)