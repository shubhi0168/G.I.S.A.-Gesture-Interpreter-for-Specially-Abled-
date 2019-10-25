import numpy as np
import cv2

glass_cascade = cv2.CascadeClassifier('/home/paa/opencv_workspace/data/cascade.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    glass = glass_cascade.detectMultiScale(gray, 50, 50)

    for (x, y, w, h) in glass:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
