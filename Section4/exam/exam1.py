import cv2 as cv
import numpy as np

img=cv.imread("face.jpeg")
mask=int('11111110',2)
new_img = np.zeros((img.shape[0],img.shape[1],3), np.uint8)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        nVal=img[i,j] & mask
        new_img[i,j] = nVal

img3=cv.hconcat([img,new_img])
# cv.imwrite('finalImage.png',img3)
cv.imshow("image",img3)
cv.waitKey(0)
# img2=cv.hconcat([img,nVal])

# cv.imwrite("img.jpeg",img2)
