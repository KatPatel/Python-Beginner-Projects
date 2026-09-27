import cv2 as cv
import numpy as np
img=np.zeros((500,500,3),dtype='uint8')
triangle=np.array([[250,50],[150,200],[350,200]])
cv.fillPoly(img,[triangle],(0,255,255))
cv.drawContours(img,[triangle],0,(0,255,0),3)
#triangle end code
cv.ellipse(img,(250,350),(100,50),0,0,360,(25,52,0),-1)
cv.ellipse(img,(250,350),(100,50),0,0,360,(255,0,0),3)
#ellipse end code
diamond=np.array([[250,220],[320,300],[250,380],[180,300]])
cv.fillPoly(img,[diamond],(8,55,201))
cv.drawContours(img,[diamond],0,(0,255,0),3)
#diamond end code
star=np.array([[100,400],[120,350],[170,350],[130,320],[150,270],[100,300],[50,270],[70,320],[30,350],[80,350]])
cv.drawContours(img,[star],0,(0,255,0),3)
cv.imshow("geometrical shapes",img)
cv.waitKey(0)
cv.destroyAllWindows()
