import cv2 as cv

mask = cv.imread('C:/Users/behrooz/PycharmProjects/VisionComputing/Section1/Mask.jpg')

thresh = 127
vid = cv.VideoCapture(0)
mask = cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
mask[mask > 127] = 255
mask[mask <= 127] = 0

while (True):
    ret, frame = vid.read()
    width = frame.shape[0]
    height = frame.shape[1]
    mask = cv.resize(mask, (height, width), interpolation=cv.INTER_AREA)
    b, g, r = cv.split(frame)
    for x in range(width):
        for y in range(height):
            pixel = mask[x, y]
            if pixel == 0:
                b[x, y] = 0
                g[x, y] = 0
                r[x, y] = 0
            else:
                pass
    frame = cv.merge((b, g, r))
    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF == ord('s'):
        break

vid.release()
# با فرض اینکه عکس اصلی را بدون gray scale انجام دهید باعث می شود که محاسبات ما بر روی ماتریس سه بعدی انجام شود و این عمل
# می شود محاسبات ما سه برابر انجام شود و سرعت نشان دادن تصویر در هر فریم بسیار کاهش پیدا خواهد کرد.
