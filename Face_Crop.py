import cv2 as cv
import numpy as np
face_cascade=cv.CascadeClassifier(cv.data.haarcascades+'haarcascade_frontalface_default.xml')
img=cv.imread("img.jpg")
grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(grey,1.3,5)
for(x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    face_crop=img[y:y+h,x:x+w]
    cv.imshow("face only",face_crop)
cv.imshow("Original Image",img)
cv.waitKey(0)
cv.destroyAllWindows()
