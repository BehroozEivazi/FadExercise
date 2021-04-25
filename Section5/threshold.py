import cv2 as cv
import numpy as np

# image = cv.imread("C:/Users/behrooz/PycharmProjects/VisionComputing/Section5/eye19.jpeg",1)
# t1,result= cv.threshold(image, 30, 255, cv.THRESH_BINARY_INV)
# cv.imshow('orginal image', image)
# cv.imshow('result1', result)
# cv.waitKey(0)
image = cv.imread("C:/Users/behrooz/PycharmProjects/VisionComputing/Section5/eye2.jpeg", 0)
blur = cv.GaussianBlur(image, (5, 5), 0)
t1, result = cv.threshold(blur, 0, 255, cv.THRESH_OTSU)
cv.imshow('orginal image', image)
cv.imshow('result1', result)
cv.waitKey(0)
