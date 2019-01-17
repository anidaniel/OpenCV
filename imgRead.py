import numpy as np 
import cv2 

#Image read and saving into 'img' variable
img = cv2.imread("download.jpg")

#Py supported window for image
cv2.namedWindow("Image",cv2.WINDOW_NORMAL)

#Image display and pop up wait function.
cv2.imshow("Image",img)
cv2.waitKey(0)
