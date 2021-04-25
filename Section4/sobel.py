import cv2 as cv
import numpy as np

img = cv.imread("./car.jpg", 0)
cv.imshow("source image", img)
result = cv.bilateralFilter(img, 3, 75, 75)
# resultX=cv.Sobel(img,cv.CV_64F,0,1,5)
# resultY=cv.Sobel(img,cv.CV_64F,1,0,5)
# cv.imshow("resultX", resultX)
result = cv.Laplacian(result, cv.CV_64F)
cv.imshow("resultY", result)

cv.waitKey(0)
