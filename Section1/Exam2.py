import cv2 as cv

image = cv.imread("C:/Users/behrooz/PycharmProjects/VisionComputing/Section1/images/k5img.jpg")
path = "C:/Users/behrooz/PycharmProjects/VisionComputing/Section1/threasholdImages/"
reng = 160

imgGrayScale = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow("gray", imgGrayScale)

imgGrayScale[imgGrayScale > reng] = 255
imgGrayScale[imgGrayScale <= reng] = 0
# Iterate ranges; find proper pixel indices; set proper color in map at these indices


cv.imwrite('{}/ThreshImg.jpg'.format(path), imgGrayScale)
cv.imshow("afterTreshold", imgGrayScale)

cv.waitKey(0)
cv.destroyAllWindows()
# docs
# اگر ما شرظ جدا سازی خودرو داخل تصویر را مبنا قرار دهیم پس آستانه ای که
# بتواند این چداسازی را بهتر انجام بدهد برای
# ما قابل قبول است که بهترین مقدار عدد های بین 120 تا 128 است


# عکس هایی که زیر 140 معمولا آستانه گذاری می شدند دارای نویز های بسیاری بودند که با این نتیجه بهترین عدد برای
# آستانه گذاری عدد بین 140 تا 160 است و بیشر شدن این عدد باعث می شود که لبه های خودرو در عکس معلوم نشود
