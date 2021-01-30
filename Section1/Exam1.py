import cv2 as cv2
import numpy as np
# read image
img = cv2.imread("D:/vision computing/First Class/car.jpg")
imgReshape = img.reshape((-1, 3))

# convert to  numpy array float32
imgToFloat = np.float32(imgReshape)

# define criteria, number of clusters(K) and apply kmeans()
# we can set for first number max and min of epsilons
criteria = (3, 10, 1.0)
K =8

ret, label, center = cv2.kmeans(imgToFloat, K, None, criteria, 10,cv2.KMEANS_RANDOM_CENTERS)

# convert image to uint8 and create orginal image with kmeans
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

cv2.imwrite("k{}image.jpg".format(K), res2)
cv2.imshow('img', res2)
cv2.waitKey(0)
cv2.destroyAllWindows()


# in blong we can see the image plot of color with kmeans

# img = cv.cvtColor(image, cv.COLOR_BGR2RGB)
# plt.imshow(img)
# plt.show()
#
# img = img.reshape((img.shape[1] * img.shape[0], 3))
#
# kmeans = KMeans(n_clusters=7)
# s = kmeans.fit(img)
#
# labels = kmeans.labels_
#
# centroid = kmeans.cluster_centers_
# labels = list(labels)
#
# print(labels)
#
# percent = []
# for i in range(len(centroid)):
#     j = labels.count(i)
#     j = j / (len(labels))
#     percent.append(j)
# # plt.pie(percent, colors=np.array(centroid / 255), labels=np.arange(len(centroid)))
# # plt.show()
#
#
#
# print(percent)
