import cv2 as cv
import numpy as np
img=cv.imread("OIP2.jpg")
cv.imshow('Image',img)

print("The shape of the images")
print(img.shape)
print("The size of the images")
print(img.size)
print("The data value of the pixel values in the images")
print(img.dtype)

px=img[100,100]
print("value of the pixel 100x100")
print(px)
blue=img[100,100,0]
print("value of blue pixel 100x100")
print(blue)
#img[:] = [255,255,255]
img[100:150,100:150]=[255,255,255]
cv.imshow('img 1',img)
cv.waitKey(0)
cv.destroyAllWindows()
