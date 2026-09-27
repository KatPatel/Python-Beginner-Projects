#geometrical shapes using open cv
import cv2 as cv
import numpy as np
#create a black image
bimg=np.zeros((512,512,3),np.uint8)
#diagonal blue line
cv.line(bimg,(0,0),(511,511),(255,0,0),5)
#format is start point,end point,colour,thickness
#draw a green rectangle
cv.rectangle(bimg,(384,0),(510,128),(0,255,0),3)
cv.rectangle(bimg,(0,0),(345,87),(45,87,212),5)
cv.circle(bimg,(289,45),94,(38,29,2),7)
cv.imshow('img',bimg)
cv.waitKey(0)
cv.destroyAllWindows()
