"""Implementation of a monocromatic scaler code

Inputs:
    - Image
    - scale
    - quantization technic
    
Output:
    - Scaled image
"""

import cv2
import functions

#path = input("Image full path: ")
path = "exemplo1.png"

img = cv2.imread(path)
if functions.isRGB(img):
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
x,y = functions.new_shape(img, 10)


#cv2.imshow('figure2',img)
#cv2.waitKey(0) 
