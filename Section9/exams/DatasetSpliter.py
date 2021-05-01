import os
import shutil

PathFiles = "D:/dataset/ds images/train/"
dir2 = "D:/dataset/ds images/data/"
cats, dogs = [], []
train_num, test_num, val_num = 0, 0, 0


def changedir(name, type, filename):
    shutil.move(PathFiles + filename, dir2 + f'{name}/{type}/' + filename)

for dirpath, dirnames, filenames in os.walk(PathFiles):
    train_num = int((len(filenames) * 0.8) / 2)
    test_num = int((len(filenames) * 0.1) / 2)
    val_num = int((len(filenames) * 0.1) / 2)
    for i in filenames:
        if 'dog' in i:
            dogs.append(i)
        if 'cat' in i:
            cats.append(i)
for i in range(0, train_num):
    cat = cats[i]
    dog = dogs[i]
    shutil.move(dirpath + cat, dir2 + 'train/cat/' + cat)
    shutil.move(dirpath + dog, dir2 + 'train/dog/' + dog)
for i in range(train_num, train_num + test_num):
    cat = cats[i]
    dog = dogs[i]
    shutil.move(dirpath + cat, dir2 + 'test/cat/' + cat)
    shutil.move(dirpath + dog, dir2 + 'test/dog/' + dog)
for i in range(train_num + test_num, len(dogs)):
    cat = cats[i]
    dog = dogs[i]
    shutil.move(dirpath + cat, dir2 + 'validation/cat/' + cat)
    shutil.move(dirpath + dog, dir2 + 'validation/dog/' + dog)

print("job done")
