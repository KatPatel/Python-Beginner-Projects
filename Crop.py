import cv2 as cv
import numpy as np
img=cv.imread("OIP6.jpg")
r=img[100:200,100:200]
r=img[300:400,300:400]
cv.imshow("copied image",img)
cv.waitKey(0)
cv.destroyAllWindows()
