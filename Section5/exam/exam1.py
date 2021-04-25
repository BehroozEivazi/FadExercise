import cv2
import numpy as np

cap = cv2.VideoCapture('D:/dataset/1.mp4')
threshold = 100


def drowRectangle(image):
    # min_x, min_y = width, height
    # max_x = max_y = 0
    #
    # for contour, hier in zip(contours, hierarchy):
    #     (x, y, w, h) = cv2.boundingRect(contour)
    #     min_x, max_x = min(x, min_x), max(x + w, max_x)
    #     min_y, max_y = min(y, min_y), max(y + h, max_y)
    #     if w > 80 and h > 80:
    #         cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    # if max_x - min_x > 0 and max_y - min_y > 0:
    #     cv2.rectangle(frame, (min_x, min_y), (max_x, max_y), (255, 0, 0), 2)
    return ""


while (True):
    ret, frame = cap.read()
    result = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    result = cv2.blur(result, (3, 3))
    result = cv2.medianBlur(result, 5)
    result = cv2.Canny(result, 100, 255)
    contours, hierarchy = cv2.findContours(result, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    # cv2.drawContours(frame, contours, -1, (255, 255, 0), 4)
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        size =w / h

        if w > 50 and h > 50 and size > 0.85 and x > 160:
            cv2.putText(frame, str(x), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 1)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
