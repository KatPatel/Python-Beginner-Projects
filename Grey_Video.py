import cv2 as cv
import numpy as np
capture=cv.VideoCapture(0)
while True:
    ret,frame=capture.read()
    grey=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    cv.imshow("Grey Video",grey)
    if cv.waitKey(1)==27:
        break
capture.release()
cv.destroyAllWindows()
