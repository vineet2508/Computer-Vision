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

while(1):
    cv2.imshow('Meranaam',img)
    k=cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    b = cv2.getTrackbarPos('B','Meranaam')
    g = cv2.getTrackbarPos('G','Meranaam')
    r = cv2.getTrackbarPos('R','Meranaam')

    img[:]=[b,g,r]
cv2.destroyAllWindows()
