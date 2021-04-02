import cv2 as cv
import numpy as np

img = cv.imread("face.jpeg", 0)
catImage = cv.imread("cat.png", 0)


def imgTobin(img):
    imgArr = []
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            binNum = np.binary_repr(img[i, j], width=8)
            imgArr.append(binNum)
    return imgArr


def sliceArr(arr):
    finalArr = []
    for i in arr:
        i = i[::-1]
        for j in range(2, 10, 2):
            num = j - 2
            finalArr.append(i[num:j])
    return finalArr


arrMask = imgTobin(catImage)
resultMask = sliceArr(arrMask)

new_img = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
counter = 0
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        str = np.binary_repr(img[i, j], width=6)
        if counter < len(resultMask):
            mask = str[0:6] + resultMask[counter]
        else:
            mask = "11111100"
        nVal = img[i, j] & int(mask, 2)
        counter += 1
        new_img[i, j] = nVal

img3 = cv.cvtColor(new_img, cv.COLOR_BGR2GRAY)
cv.imwrite('convImage.png', img3)
cv.imshow('finalImage', img3)
cv.waitKey(0)
