import os

import cv2
import histogram_calc
import KnnClassifier

source_image = cv2.imread('D:/car.jpg')
print(source_image.shape)
prediction = 'n.a.'

PATH = './training.data'

if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
    print ('training data is ready, classifier is loading...')
else:
    histogram_calc.training()


histogram_calc.histogram(source_image,True)
prediction = KnnClassifier.main('training.data', 'test.data')
print(prediction)
cv2.imwrite("{}.png".format(prediction[0]), source_image)
cv2.imshow("{}".format(prediction[0]), source_image)
cv2.waitKey(0)
