import cv2 as cv

mask = cv.imread('C:/Users/behrooz/PycharmProjects/VisionComputing/Section1/Mask.jpg')


def grayToBinary(img, rang):
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img[img > rang] = 255
    img[img <= rang] = 0
    return img


mask = grayToBinary(mask, 140)
vid = cv.VideoCapture(0)

while (True):

    ret, frame = vid.read()
    # frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # if we comment top line we should change bitwise function and we can change the gray scale  image to rgb
    width = frame.shape[0]
    height = frame.shape[1]
    mask = cv.resize(mask, (height, width), interpolation=cv.INTER_AREA)
    # result = cv.bitwise_and(frame, mask)
    # top line for base image gray scale
    result = cv.bitwise_and(frame,frame, mask=mask)
    cv.imshow('frame', result)
    if cv.waitKey(1) & 0xFF == ord('s'):
        break

vid.release()
