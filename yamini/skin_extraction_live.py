import cv2

cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    ycrcb=cv2.cvtColor(frame,cv2.COLOR_BGR2YCrCb)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    b,g,r = cv2.split (frame)
    Y,Cr,Cb=cv2.split(ycrcb)
    H,S,V=cv2.split(hsv)
    S=S/(H+S+V)
    
    result=((0.0 <=H)*(H <= 50.0)*(0.23 <= S)*(S<= 0.68)*(r > 95)*(g > 40)*(b > 20)*(r > g)*(r > b)*(abs(r - g)> 15)+(r > 95)*(g > 40)*(b > 20)*(r > g)*(r > b)*(abs(r - g ) > 15)*(Cr > 135)*(Cb > 85)*(Y > 80)*(Cr <= (1.5862*Cb)+20)*(Cr>=(0.3448*Cb)+76.2069)*(Cr >= (-4.5652*Cb)+234.5652)*(Cr <= (-1.15*Cb)+301.75)*(Cr <= (-2.2857*Cb)+432.85))*255
    result=cv2.merge((result,result,result))
    img2=frame&result
    cv2.imwrite('image.jpeg',img2)
    img1=cv2.imread('image.jpeg')
    cv2.imshow('Merged Output',img1)
    
    c = cv2.waitKey(1)    #will break the loop when pressed enter key
    if c == 13:
        break

cap.release()
cv2.destroyAllWindows()
