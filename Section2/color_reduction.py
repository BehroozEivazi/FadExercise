import cv2 as cv
import numpy as np
from scipy.cluster.vq import kmeans2

if __name__ == "__main__" :
    img = cv.imread(r"C:\Users\Mhsafavian\Desktop\Amoozeshgah\8cef236c1c21c4.jpg")

    k=8
    h=img.shape[0]
    w=img.shape[1]

    img_reshaped = np.reshape(img, (w* h, 3))

    img_reshaped_float = img_reshaped.astype(float)
    centorid , labels = kmeans2(img_reshaped_float, k)

    print("size of labels {}".format(labels.shape))

    reduced_list =[]

    for i in range(labels.shape[0]) :
        reduced_list.append(centorid[labels[i]])

    reduced_array = np.asarray(reduced_list)
    reduced_image_float=np.reshape (reduced_array, (h,w,3))
    img_reduced = reduced_image_float.astype(dtype='uint8')

    cv.imshow("reduced image", img_reduced)
    cv.waitKey()




