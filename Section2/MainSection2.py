import cv2 as cv
import numpy as np

# img = cv.imread("C:/Users/behrooz/PycharmProjects/VisionComputing/Section2/img/Fig0304(a)(breast_digital_Xray).tif")
#
# img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# img_negetive = 255 - img
# cv.imshow("my image", img_negetive)
# cv.waitKey(0)
#
img = cv.imread("C:/Users/behrooz/PycharmProjects/VisionComputing/Section2/img/Fig0305(a)(DFT_no_log).tif", 0)
cv.imshow("Orginal Image", img)
img_log = np.log(1 + np.float32(img))
cv.imshow("Transform", img_log)
cv.waitKey(0)
