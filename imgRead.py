'''Loading an image (of me :P ),
    into and displaying into a created window'''
import numpy as np 
import cv2 

#Image read and saving into 'img' variable
img = cv2.imread("download.jpg")

#Py supported window for image
cv2.namedWindow("Image",cv2.WINDOW_NORMAL)

#Image display and pop up wait function.
cv2.imshow("Image",img)
cv2.waitKey(0)

#kills the window(s)
cv2.destroyAllWindows()