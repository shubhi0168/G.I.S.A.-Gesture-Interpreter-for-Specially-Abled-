import cv2
import numpy as np
img=cv2.imread("/home/paa/my.jpg")

print(img)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
hsv_mask=cv2.inRange(hsv,(0,15,0),(17,170,255))
hsv_mask=cv2.morphologyEx(hsv_mask,cv2.MORPH_OPEN,np.ones((3,3)))

img_ycrcb= cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
ycrcb_mask = cv2.inRange(img_ycrcb, (0, 135, 85), (255,180,135))
ycrcb_mask = cv2.morphologyEx(ycrcb_mask, cv2.MORPH_OPEN, np.ones((3,3)))

global_mask=cv2.bitwise_and(ycrcb_mask,hsv_mask)
global_mask=cv2.medianBlur(global_mask,3)
global_mask = cv2.morphologyEx(global_mask, cv2.MORPH_OPEN, np.ones((3,3)))



hsv_result = cv2.bitwise_not(hsv_mask)
ycrcb_result = cv2.bitwise_not(ycrcb_mask)
global_result = cv2.bitwise_not(global_mask)

cv2.imwrite("1_HSV.jpg",hsv_result)
cv2.imwrite("2_YCbCr.jpg",ycrcb_result)
cv2.imwrite("3_global_result.jpg",global_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
