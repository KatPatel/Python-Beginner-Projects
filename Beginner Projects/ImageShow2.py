#if else condition with images
import cv2 as cv
import numpy as np

choice=input("enter c for colour image and g for grey image")

Image2= cv.imread("img.jpg")
greyscale2= cv.imread("img.jpg",0)
#print("image type:",type(Image2))
#print("Image Shape:",Image2.shape)
if choice=='c':
    cv.imshow("colour image", Image2)
elif choice== 'g':
    cv.imshow("greyimg",greyscale2)
else:
    print("invalid choice")
cv.waitKey(0)
cv.destroyAllWindows()
