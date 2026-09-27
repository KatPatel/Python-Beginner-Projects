import cv2 as cv
import numpy as np
video=cv.VideoCapture("video.mp4")
while (video.isOpened()):
    ret,frame=video.read()
    cv.imshow("frame",frame)
    key=cv.waitKey(1)
    if key==27: # esc key
        break
video.release()
cv.destroyAllWindows()
