import numpy as np 
import cv2

#Image read and saving into 'img' variable
img = cv2.imread("download.jpg", 1) #with pass value 1 for reading the image as default colors
'''
Under Python IDLE if we run this:
>>> img  #It'll return the found pixels from the image
array([[[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       ...,

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]]], dtype=uint8)

>>> type(img)
<class 'numpy.ndarray'>
>>> len(img)
225
>>> len(img[0]) #Returns pixels
225
>>> len(img[0][0]) #Returns color ratio
3
>>> img.shape  #This returns (HRows,Columns,Color )
(225, 225, 3) 
>>> img.dtype 
dtype('uint8') #Tells us 2**8 or 256 in each pixel ''' 

