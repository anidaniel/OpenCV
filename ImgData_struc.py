import numpy as np 
import cv2 

#printing black matrix
black = np.zeros([150,200,1],'uint8')
cv2.imshow("Black",black)
print(black[0,0,:])

#validated invalid matrix :P 
ones = np.ones([150,200,3],'uint8')
cv2.imshow("Ones",ones)
print(ones[0,0,:])

#white matrix
white = np.ones([150,200,3],'uint16')
white *= (2**16-1)
cv2.imshow("White",white)
print(white[0,0,:])

#BGR FORMAT BLUE matrix
color1 = ones.copy()    #copying whole attr from var ones and making it unique both attr and mem to color1
color1[:,:,] = (255,0,0) #BGR FORMAT
cv2.imshow("Blue",color1)
print(color1[0,0,:])

#BGR FORMAT GREEN matrix
#color2 = np.ones([150,200,3],'uint8')
color2 = ones.copy()
color2[:,:,] = (0,255,0) #BGR FORMAT
cv2.imshow("Green",color2)
print(color2[0,0,:])

#BGR FORMAT RED matrix
#color3 = np.ones([150,200,3],'uint8')
color3 = ones.copy()
color3[:,:,] = (0,0,255) #BGR FORMAT
cv2.imshow("Red",color3)
print(color3[0,0,:])

cv2.waitKey(0)
cv2.destroyAllWindows()

''' CODE RUN : 
    D:\Projects\OpenCV> python .\ImgData_struc.py
        [0]
        [1 1 1]
        [65535 65535 65535]
        [255   0   0]
        [  0 255   0]
        [  0   0 255] '''