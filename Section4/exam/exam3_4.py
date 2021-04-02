# import cv2 as cv
# import numpy as np
#
# img = cv.imread("convImage.png", 0)
#
# def imgTobin(img):
#     imgArr = []
#     for i in range(img.shape[0]):
#         for j in range(img.shape[1]):
#             binNum = np.binary_repr(img[i, j], width=8)
#             str = binNum[-2:]
#             imgArr.append(str)
#     return imgArr
#
# arrMask = imgTobin(img)
#
# lastArr = []
#
# str = ''
# for i in arrMask:
#     str = str + i
#     if (len(str) == 8):
#         str = str[::-1]
#         lastArr.append(str)
#         str = ''
#
# new_img = np.zeros((img.shape[0], img.shape[1], 1), np.uint8)
#
# for i in range(0, img.shape[0]):
#     for j in range(0, img.shape[1]):
#         mask = int(lastArr[i], 2)
#         new_img[i, j] = mask
#
# cv.imshow('img', new_img)
# cv.waitKey(0)
import cv2
import numpy as np
import random


def encrypt():
    # img1 and img2 are the
    # two input images
    img1 = cv2.imread('face.jpeg')
    img2 = cv2.imread('cat.png')

    for i in range(img2.shape[0]):
        for j in range(img2.shape[1]):
            for l in range(3):
                # v1 and v2 are 8-bit pixel values
                # of img1 and img2 respectively
                v1 = format(img1[i][j][l], '08b')
                v2 = format(img2[i][j][l], '08b')

                # Taking 4 MSBs of each image
                v3 = v1[:6] + v2[:2]

                img1[i][j][l] = int(v3, 2)

    cv2.imwrite('pic3in2.png', img1)


def decrypt():
    # Encrypted image
    img = cv2.imread('pic3in2.png')
    width = img.shape[0]
    height = img.shape[1]

    # img1 and img2 are two blank images
    img1 = np.zeros((width, height, 3), np.uint8)
    img2 = np.zeros((width, height, 3), np.uint8)

    for i in range(width):
        for j in range(height):
            for l in range(3):
                v1 = format(img[i][j][l], '08b')
                v2 = v1[:6] + chr(random.randint(0, 1) + 48) * 6
                v3 = v1[2:] + chr(random.randint(0, 1) + 48) * 2

                # Appending data to img1 and img2
                img1[i][j][l] = int(v2, 2)
                img2[i][j][l] = int(v3, 2)

    # These are two images produced from
    # the encrypted image
    cv2.imshow('pic2_re.png', img1)
    cv2.imshow('pic3_re.png', img2)
    cv2.waitKey(0)
decrypt()