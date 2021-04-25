import cv2
import numpy as np
import os

path = 'C:/Users/behrooz/PycharmProjects/VisionComputing/pdf/FVC2002/DB1_B'
SavePath = 'D:/dataset/FingerVector/'

def drow_rectangle(source, name):
    image = cv2.imread(source)
    result = cv2.blur(image, (3, 3))
    retval, thresh_gray = cv2.threshold(result, thresh=127, maxval=255, type=cv2.THRESH_BINARY)
    result = cv2.Canny(thresh_gray, 100, 255)
    pts = np.argwhere(result > 0)
    if (len(pts) > 0):
        y1, x1 = pts.min(axis=0)
        y2, x2 = pts.max(axis=0)
        tagged = cv2.rectangle(image.copy(), (x1, y1), (x2, y2), (125, 125, 125), 1, cv2.LINE_AA)
        cv2.imwrite(SavePath + name , tagged)
    else:
        cv2.imwrite(SavePath + name , image)

for f in os.listdir(path):
    drow_rectangle(path + '/' + f, f)

print("Job Done")
