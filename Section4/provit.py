import cv2 as cv
import numpy as np

img = cv.imread("C:/Users/behrooz/PycharmProjects/VisionComputing/Section4/bill.jpeg", 0)
cv.imshow("source image", img)

result=cv.bilateralFilter(img,9,75,75)
# kernel = np.array([[-1,0, 1],
#                    [-1, 0, 1],
#                    [-1, 0, 1]])
kernel = np.array([[-1,-1, -1],
                   [0, 0, 0],
                   [1, 1, 1]])
result = cv.filter2D(result, -1, kernel=kernel)
cv.imshow("change image", result)
cv.waitKey(0)
