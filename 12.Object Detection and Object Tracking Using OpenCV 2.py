import numpy as np
import cv2

def func(x):
    print(x)
    
cv2.namedWindow('Meranaam')
#This namedWindow is used to create a window with a name
cv2.createTrackbar('CP','Meranaam', 10, 400, func)

switch='Colored/ Gray'
cv2.createTrackbar(switch,'Meranaam', 0, 1, func)
while(1):
    img=cv2.imread('lena.jpg')

    pos=cv2.getTrackbarPos('CP','Meranaam')
    font=cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(img,str(pos),(50,150), font, 4,(0,0,255),4)
    
    k=cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    s= cv2.getTrackbarPos(switch,'Meranaam')

    if s == 0:
        pass
    else:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    cv2.imshow('Meranaam',img)

cv2.destroyAllWindows()

