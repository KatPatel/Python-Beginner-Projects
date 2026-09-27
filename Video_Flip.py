import cv2 as cv
import numpy as np
capture=cv.VideoCapture(0)
while True:
    ret,frame=capture.read()
    flip=cv.flip(frame,1)
    cv.imshow("Flip The Video",flip)
    if cv.waitKey(1)==ord('q'):
        break
capture.release()
cv.destroyAllWindows()
    
