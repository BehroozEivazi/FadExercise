import cv2 as cv
import numpy as np

img = cv.imread('D:/vision computing/datasets/night.jpeg')
cv.imshow('my Image', img)
cv.waitKey(0)

img
width = img.shape[0]
height = img.shape[1]
chan = img.shape[2]

img_blue = img[:, :, 0]
img_green = img[:, :, 1]
img_red = img[:, :, 2]

img_reconstruct = np.zeros(img.shape, 'uint8')
# ax

img_reconstruct[:, :, 0] = img_green = img[:, :, 0]
img_reconstruct[:, :, 1] = img_green = img[:, :, 1]
img_reconstruct[:, :, 2] = img_green = img[:, :, 2]
cv.imshow("Recontruct Image", img_reconstruct)
cv.waitKey(0)
b, g, r = cv.split(img)

img_reconstruct = cv.merge((b, g, r))
cv.imshow("image sample", img_reconstruct)
cv.waitKey(0)
