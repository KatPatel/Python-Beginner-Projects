# This is not RGB format as many people knpw it as but in this code it is BGR format
import cv2 as cv
import numpy as np
img=cv.imread("img.jpg")
b,g,r=cv.split(img)
zeros=np.zeros_like(b)
blue_img=cv.merge([b,zeros,zeros])
green_img=cv.merge([zeros,g,zeros])
red_img=cv.merge([zeros,zeros,r])
cv.imshow("Blue Image",blue_img)
cv.imshow("Green Image",green_img)
cv.imshow("Red Image",red_img)
cv.waitKey(0)
cv.destroyAllWindows()
