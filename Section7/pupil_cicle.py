import numpy as np
import cv2 as cv

# morph_size = 11
morph_size = 25
imageBGR = cv.imread('eye3.jpeg', 1)
imageGRY = cv.imread('eye3.jpeg', 0)

img_copy = imageGRY.copy()
ret, thresh = cv.threshold(img_copy, 50, 255, cv.THRESH_BINARY_INV)

se = np.ones((morph_size, morph_size), np.uint8)
img_morph = cv.morphologyEx(thresh, cv.MORPH_OPEN, se)

countours, hierarchy = cv.findContours(img_morph, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(img_copy, countours, -1, (0, 0, 255), 3)

(x, y), rad = cv.minEnclosingCircle(countours[0])

# ba ye halghe for bar asas masahatesh ono takmil mikonim
cv.circle(imageBGR, (int(x), int(y)), int(rad), (0, 0, 255), 2)
cv.imshow('morph', img_morph)
cv.imshow('thresh', thresh)
cv.imshow('copy', img_copy)
cv.imshow('image', imageBGR)
cv.waitKey(0)
