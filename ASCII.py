import cv2 as cv
import numpy as np
img=cv.imread('OIP.jpg')
gimg=cv.imread('OIP.jpg',0)
cv.imshow('colour image',img)
cv.imshow('grey image',gimg)
key=cv.waitKey(0)
if key==27:
    cv.destroyAllWindows()
elif key==ord('s'):
    cv.imwrite('grey_OIP.jpg',gimg)
    cv.destroyAllWindows()
