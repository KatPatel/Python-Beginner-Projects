#read the image
import cv2 as cv
import numpy as np
img=cv.imread('OIP.jpg')
img1=cv.imread('OIP.jpg',0)


cv.imshow('OIP',img)
cv.imshow('GreyScale',img1)


cv.imwrite('GreyOIP.jpg',img1)

cv.waitKey(0)
cv.destroyAllWindows()
