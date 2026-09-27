import cv2 as  cv
import numpy as np
capture=cv.VideoCapture(0)
while True:
    ret,frame=capture.read()
    cv.imshow("Web Cam",frame)
    if cv.waitKey(1)==27:
        break
capture.release()
cv.destroyAllWindows()
