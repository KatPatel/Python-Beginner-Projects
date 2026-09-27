# ASCI stands for American Standard Code for Information Interchange it is basicaly machine code but for the keys on your keyboard e.g. key==27 relates to the escape key
import cv2 as cv
import numpy as np
img=cv.imread('img.jpg')
gimg=cv.imread('img.jpg',0)
cv.imshow('colour image',img)
cv.imshow('grey image',gimg)
key=cv.waitKey(0)
if key==27: # This key is the esc key
    cv.destroyAllWindows() # closes the image
elif key==ord('s'):  # This if statement will save the grey image as a file on your device
    cv.imwrite('grey_img.jpg',gimg)
    cv.destroyAllWindows()
