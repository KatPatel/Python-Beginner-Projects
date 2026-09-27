import cv2 as cv
import numpy as np
img=cv.imread("img.jpg")
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("OIP.jpg",img)
cv.imshow("HSV",hsv)
