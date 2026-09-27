import cv2 as cv
import numpy as np
img=cv.imread("OIP.jpg")
grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("OIP.jpg",img)
cv.imshow("Grey Image",grey)
cv.waitKey(0)
cv.destroyAllWindows()
