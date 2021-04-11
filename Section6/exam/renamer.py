import os

path="C:/Users/behrooz/Desktop/Covid19-Face-Mask-Detector-master/dataset/n"

counter = 0
for i, filename in enumerate(os.listdir(path)):
        counter = counter + 1
        print(str(counter))


