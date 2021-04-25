import numpy as np
import time
import cv2 as cv
from matplotlib import pyplot as plt
import imutils



if __name__ == "__main__":
    imgPath = "D:/vision computing/First Class/car.jpg"
    img = cv.imread(imgPath,1)
    h, w = img.shape[:2]
    cent = (w // 2, h // 2)
    M = cv.getRotationMatrix2D(cent, 45, 1.0)
    rot_img = cv.warpAffine(img, M, (w, h))

    cv.imshow("img", img)
    cv.imshow("rotated image", rot_img)

    cv.waitKey(0)

