import cv2
import numpy as np
img = cv2.imread('hand2.jpeg',1)
ycrcb=cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
b,g,r = cv2.split (img)
Y,Cr,Cb=cv2.split(ycrcb)
H,S,V=cv2.split(hsv)
S=S/(H+S+V)
result=((0.0 <=H)*(H <= 50.0)*(0.23 <= S)*(S<= 0.68)*(r > 95)*(g > 40)*(b > 20)*(r > g)*(r > b)*(abs(r - g)> 15)+(r > 95)*(g > 40)*(b > 20)*(r > g)*(r > b)*(abs(r - g ) > 15)*(Cr > 135)*(Cb > 85)*(Y > 80)*(Cr <= (1.5862*Cb)+20)*(Cr>=(0.3448*Cb)+76.2069)*(Cr >= (-4.5652*Cb)+234.5652)*(Cr <= (-1.15*Cb)+301.75)*(Cr <= (-2.2857*Cb)+432.85))*255
cv2.imwrite('image.jpeg',result)
img1=cv2.imread('image.jpeg')
cv2.imshow('Merged Output',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
