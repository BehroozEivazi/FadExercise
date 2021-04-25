import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# filter guasian opencv

# img = cv.imread("C:/Users/behrooz/PycharmProjects/VisionComputing/Section4/eye.jpeg")
# cv.imshow("source image", img)
#
# result=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
# cv.imshow("blur image", result)
#
# cv.waitKey(0)


img = cv.imread("C:/Users/behrooz/PycharmProjects/VisionComputing/Section4/face.jpeg")
cv.imshow("source image", img)
result = cv.medianBlur(img,9)
cv.imshow("img", result)
cv.waitKey(0)
