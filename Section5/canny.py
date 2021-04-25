import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread("C:/Users/behrooz/PycharmProjects/VisionComputing/Section5/eye.jpeg")
result=cv.bilateralFilter(image,15,150,150)
# result=cv.medianBlur(image,7)
# aval bayad ro ax asli filter bilat ya guasi ya harchi ro bezanim badesh filter canny ro bezanim
edge = cv.Canny(result, 100, 200)
cv.imshow('after blur',result)
cv.imshow('canny result',edge)
cv.imshow("image", image)
cv.waitKey(0)
