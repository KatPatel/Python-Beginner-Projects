import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
#Displaying an Image
#img=cv.imread("OIP.jpg")
#img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
#plt.imshow(img)
#plt.title("OIP.jpg")
#plt.show()

#Display Greyscale Image
#img=cv.imread("OIP.jpg",0)
#plt.imshow(img,cmap="grey")
#plt.title("Grey Image")
#plt.show()

#Plot multiple images using mat plot library
img=cv.imread("img.jpg")
grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blur=cv.GaussianBlur(img,(15,15),0)
plt.subplot(1,2,1)
plt.imshow(cv.cvtColor(img,cv.COLOR_BGR2RGB))
plt.title("img.jpg")
plt.subplot(1,2,2)
plt.imshow(grey,cmap="grey")
plt.title("Grey")
plt.subplot(1,3,2)
plt.imshow(cv.cvtColor(blur,cv.COLOR_BGR2RGB))
plt.title("Blurred Image")
plt.show()
