import cv2 as cv
import numpy as np
capture=cv.VideoCapture("piano.mp4")
while True:
    ret,frame=capture.read()
    if not ret:
        break
    cv.imshow("Video Play",frame)
    if cv.waitKey(25)==ord('q'):
        break
capture.release()
cv.destroyAllWindows()
    
