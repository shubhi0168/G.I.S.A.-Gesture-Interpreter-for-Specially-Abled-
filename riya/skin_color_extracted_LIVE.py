#skin colour extracted in live cam

import cv2
import numpy as np

def extract_skin(img,img_HSV,img_YCrCb):
    
    B,G,R=cv2.split(img)
    H,S,V=cv2.split(img_HSV)
    Y,Cr,Cb=cv2.split(img_YCrCb)
    
    cond_img= (((H>=0.0)*(H<= 50.0)*(S>=0.23)*(S<= 0.68)*(R > 95)*(G > 40)*(B > 20)*(R > G)*(R > B)*(abs(R - G) > 15))+
    ((R > 95)*(G > 40)*(B > 20)*(R > G)*(R > B)*(abs(R - G) > 15)*(Cr > 135)*(Cb > 85)* (Y > 80)*(Cr <= (1.5862*Cb)+20)*(Cr >=(0.3448*Cb)+76.2069)*(Cr >= (-4.5652*Cb)+234.5652)*(Cr <= (-1.15*Cb)+301.75)*(Cr <= (-2.2857*Cb)+432.85)))*255
    
    cv2.imwrite('skin_extracted_img.jpeg',cond_img)
    skin_img_white=cv2.imread('skin_extracted_img.jpeg')
    skin_color_img=img&skin_img_white
    return skin_color_img



cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img_YCrCb=cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)

    
    skin_img=extract_skin(img,img_HSV,img_YCrCb)
    cv2.imshow('Skin Extraction',skin_img)
    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break
    
    
    
cap.release()
cv2.destroyAllWindows()
