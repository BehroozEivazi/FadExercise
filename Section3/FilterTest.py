import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("D:/vision computing/First Class/car.jpg", 0)
# cv.imshow("before conv", img)
# # cv.waitKey(0)
# kernel = np.array([[1, 1, 1, 1, 1, 1],
#                    [1, 1, 1, 1, 1, 1],
#                    [1, 1, 1, 1, 1, 1],
#                    [1, 1, 1, 1, 1, 1],
#                    [1, 1, 1, 1, 1, 1], ])
kernel = np.ones((3, 3), np.float64) / 25

kernel = kernel / sum(kernel)
result = cv.filter2D(img, -1, kernel=kernel)

# cv.imshow('result',result)
# cv.imwrite('result.png',result)
# cv.waitKey(0)
# in paiin yani 1*2 tasvir 1
plt.subplot(121), plt.imshow(img, 'gray'), plt.title("Orginal Image")
plt.subplot(122), plt.imshow(result, 'gray'), plt.title("Filtered Image")
plt.show()
