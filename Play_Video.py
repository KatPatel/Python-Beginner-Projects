import cv2 as cv
import numpy as np
video=cv.VideoCapture("No.6 Mazurka In A Minor Op.7 No.2.mp4")
while (video.isOpened()):
    ret,frame=video.read()
    cv.imshow("frame",frame)
    key=cv.waitKey(1)
    if key==27:
        break
video.release()
cv.destroyAllWindows()
