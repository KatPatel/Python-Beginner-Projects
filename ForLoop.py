#for loop
import cv2 as cv
import numpy as np

images=["OIP2.jpg","OIP.jpg","OIP3.jpg","OIP4.jpg", "Grey OIP"]
for i in range(5):
    for j in images:
        img=cv.imread(j)
        if img is None:
            continue
        cv.imshow("repeating images",img)
        cv.waitKey(2000)
        cv.destroyAllWindows()
