#while loop
import cv2 as cv
import numpy as np

img=["OIP.jpg","OIP2.jpg","OIP3.jpg","OIP4.jpg","Grey OIP.jpg"]
i=0
while True:
    image=cv.imread(img[i])
    if image is None:
        break
    cv.imshow("press n for next q to quit",image)
    key= cv.waitKey(0)
    cv.destroyAllWindows()

    if key== ord('n'):
        i=(i+1)%len(img)
    elif key==ord('q'):
        break
