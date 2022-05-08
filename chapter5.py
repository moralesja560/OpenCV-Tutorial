#warp perspective
import cv2
import numpy as np

img = cv2.imread("resources/box.jpg")

print(f"image height: {img.shape[0]} \nimage width: {img.shape[1]}")

#the goal of warping an image is to flatten as much as possible a relevant region

#this value are entered to guess the new image ratio, change to avoid enlarged/distorted picture.
width,height = 1000,600
#upper left, upper right, lower left and lower right
#for cropped:        3    1                             4   2
pts1 = np.float32([[145,1762],[1327,1904],[209,2344],[1414,2474]])

pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
#cropping
imgCropped = img[1762:2500,145:1400]
imgoutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("original",imgCropped)
cv2.imshow("output",imgoutput)

cv2.waitKey(0)