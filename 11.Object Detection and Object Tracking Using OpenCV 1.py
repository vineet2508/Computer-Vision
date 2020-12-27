import numpy as np
import cv2
img=np.zeros((300,512,3),np.uint8)

def func(x):
    print(x)
    
cv2.namedWindow('Meranaam')
#This namedWindow is used to create a window with a name
cv2.createTrackbar('B','Meranaam', 0, 255, func)
cv2.createTrackbar('G','Meranaam', 0, 255, func)
cv2.createTrackbar('R','Meranaam', 0, 255, func)

switch='0 : OFF\n 1 : ON'
cv2.createTrackbar(switch,'Meranaam', 0, 1, func)
while(1):
    cv2.imshow('Meranaam',img)
    k=cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    b = cv2.getTrackbarPos('B','Meranaam')
    g = cv2.getTrackbarPos('G','Meranaam')
    r = cv2.getTrackbarPos('R','Meranaam')
    s = cv2.getTrackbarPos(switch,'Meranaam')
    if s == 0:
        img[:] = 0
    else:
        img[:]=[b,g,r]
cv2.destroyAllWindows()
