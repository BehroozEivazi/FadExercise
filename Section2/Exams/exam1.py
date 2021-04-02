import cv2 as cv

# this exam for gama image negative

c = 25
img = cv.imread("C:/Users/behrooz/PycharmProjects/VisionComputing/Section2/img/Fig0305(a)(DFT_no_log).tif", 1)

cv.imshow("orginal image", img)

gama_img = c * (img ** 2)
cv.imwrite('images/image{}.png'.format(c), gama_img)
cv.imshow("Gama Image", gama_img)
cv.waitKey(0)
