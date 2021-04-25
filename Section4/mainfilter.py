import cv2 as cv
import numpy as np

img = cv.imread("C:/Users/behrooz/PycharmProjects/VisionComputing/Section4/eye.jpeg", 1)
cv.imshow("source image", img)
A=4
kernel =np.array([[0, -1,0],
                   [-1,A+4, -1],
                   [0,- 1,0], ])
result=cv.filter2D(img,-1,kernel=kernel)
# avalin adad kernele dovomin va sevomi
# result=cv.bilateralFilter(img,9,75,75)
cv.imshow("change image", result)
cv.waitKey(0)