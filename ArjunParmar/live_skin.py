import cv2
import numpy as np


def skin_detect(img):

    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    y = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    new = np.zeros((img.shape[0], img.shape[1]))
    row = img.shape[0]
    cols = img.shape[1]

    for i in range(row):
        for j in range(cols):
            B[i][j] = img[i][j][0]
            G[i][j] = img[i][j][1]
            R[i][j] = img[i][j][2]
            x[i][j] = R[i][j] + G[i][j] + B[i][j]
            h[i][j] = hsv[i][j][0]
            s[i][j] = hsv[i][j][1]
            v[i][j] = hsv[i][j][2]
            s[i][j] = s[i][j] / (h[i][j] + s[i][j] + v[i][j])
            Y[i][j] = y[i][j][0]
            Cr[i][j] = y[i][j][1]
            Cb[i][j] = y[i][j][2]

    for i in range(row):
        for j in range(cols):

            # B = img[i][j][0]
            # G = img[i][j][1]
            # R = img[i][j][2]
            # x = R + G + B
            # h = hsv[i][j][0]
            # s = hsv[i][j][1]
            # v = hsv[i][j][2]
            # s = s / (h + s + v)
            # Y = y[i][j][0]
            # Cr = y[i][j][1]
            # Cb = y[i][j][2]
            if (((0.0 <= h[i][j] <= 50.0 and 0.23 <= s[i][j] <= 0.68 and R[i][j] > 95 and G[i][j] > 40 and B[i][j] > 20 and R[i][j] > G[i][j] and R[i][j]> B[i][j] and abs(
                R[i][j] - G[i][j]) > 15)) or ((R[i][j]> 95) and (G[i][j]> 40) and (B > 20) and (R > G) and (R > B) and (abs(R - G) > 15) and (
                Cr > 135) and (Cb > 85) and (Y > 80) and (Cr <= (1.5862 * Cb) + 20) and (
                                      Cr >= ((0.3448 * Cb) + 76.2069)) and (Cr >= ((-4.5652 * Cb) + 234.5652)) and (
                                      Cr <= ((-1.15 * Cb) + 301.75))) and (Cr <= ((-2.2857 * Cb) + 432.85))):
                    new[i][j] = 1
            else:
                new[i][j] = 0

    for i in range(row):
        for j in range(cols):
            if (new[i][j] == 0):
                img[i][j][0] = 0
                img[i][j][1] = 0
                img[i][j][2] = 0

    return img


cap = cv2.VideoCapture(1)
while True:
        ret, frame = cap.read()
        frame=cv2.resize(frame,(300,300))
        skin = skin_detect(frame)
        cv2.imshow("skin", skin)
        if cv2.waitKey(1) == 13:  # 13 is the Enter Key
            break


cap.release()
cv2.destroyAllWindows()
