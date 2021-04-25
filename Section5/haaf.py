import cv2 as cv
import numpy as np

image = cv.imread("C:/Users/behrooz/PycharmProjects/VisionComputing/Section5/sudoko.jpeg")
# image = cv.imread("sudoko.jpeg")

edgeCanny = cv.Canny(image, 100, 255)
lines = cv.HoughLinesP(edgeCanny, 1, np.pi / 180, 15, 30, 12)
for i in range(len(lines)):
    for x1, y1, x2, y2 in lines[i]:
        cv.line(image, (x1, y1), (x2, y2),(0,100,255),2)


cv.imshow("canny output", edgeCanny)
cv.imshow('orginal', image)
cv.waitKey(0)
