import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread(r"C:\Users\Mhsafavian\Desktop\Amoozeshgah\Lake.jpg",1)
cv.imshow("source image", img)

f_size = 5
# fil =np.ones((f_size,f_size), np.float64) / (f_size*f_size)
fil =  (1/49) * np.array([[1,1,1,1,1,1,1],
                         [1,1,1,1,1,1,1],
                         [1,1,1,1,1,1,1],
                         [1,1,1,1,1,1,1],
                         [1,1,1,1,1,1,1],
                         [1,1,1,1,1,1,1],
                         [1,1,1,1,1,1,1]
                        ])
result = cv.filter2D(img, -1, fil)

cv.imshow("result", result)
cv.imwrite("result.png", result)
cv.waitKey(0)

plt.subplot(121),plt.imshow(img,'gray') , plt.title("Original image")
plt.subplot(122),plt.imshow(result, 'gray'),plt.title("filtered image")

plt.show()


