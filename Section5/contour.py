from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse
import random as rng

rng.seed(12345)
threshold = 100

def draw_contor():

    canny_output = cv.Canny(src_gray, threshold, threshold * 2)
    # cv.imshow("canny", canny_output)
    # cv.waitKey(0)
    contours, hierarchy = cv.findContours(canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    contours_poly = [None] * len(contours)
    boundRect = [None] * len(contours)
    centers = [None] * len(contours)
    radius = [None] * len(contours)

    for i, c in enumerate(contours):
        contours_poly[i] = cv.approxPolyDP(c, 3, True)
        # boundRect[i] = cv.boundingRect(contours_poly[i])
        centers[i], radius[i] = cv.minEnclosingCircle(contours_poly[i])

    drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)

    for i in range(len(contours)):
        color = (rng.randint(0, 256), rng.randint(0, 256), rng.randint(0, 256))
        area = cv.contourArea(contours_poly[i])
        if area >400 :
            print("area = {}".format(area))
            cv.drawContours(drawing, contours_poly, i, color)
            cv.circle(drawing, (int(centers[i][0]), int(centers[i][1])), int(radius[i]), color, 2)

    cv.imshow('Contours', drawing)
    cv.waitKey(0)

src = cv.imread(r'eye2.jpeg')

# Convert image to gray and blur it
src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
src_gray = cv.blur(src_gray, (3, 3))

src_gray = cv.medianBlur(src_gray, 5)
cv.imshow("source", src)
cv.waitKey(10)
max_thresh = 255
# cv.createTrackbar('Canny thresh:', source_window, thresh, max_thresh, thresh_callback)
# thresh_callback(thresh)
draw_contor()
cv.waitKey()