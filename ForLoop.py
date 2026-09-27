#for loop
import cv2 as cv
import numpy as np

images=["img.jpg","img2.jpg","img3.jpg","img4.jpg", "Grey Image"]
for i in range(5):
    for j in images:
        img=cv.imread(j)
        if img is None:
            continue
        cv.imshow("repeating images",img)
        cv.waitKey(2000)
        cv.destroyAllWindows()
