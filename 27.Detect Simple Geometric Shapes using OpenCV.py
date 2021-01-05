import numpy as np
import cv2
img = cv2.imread('shapes.png')
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh = cv2.threshold(imggray,240,255,cv2.THRESH_BINARY)
contours,_ =cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour,True),True)
    cv2.drawContours(img, [approx], 0,(255,0,0),5)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 15
    if len(approx) == 3:
        cv2.putText(img,'Traingle',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,200))
    elif len(approx) == 4:
        x1,y1,w,h = cv2.boundingRect(approx)
        aspectRatio = float(w)/h
        print(aspectRatio)
        if aspectRatio >= 0.90 and aspectRatio <= 1.1:
            cv2.putText(img,'Square',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,200))
        else:
            cv2.putText(img,'Rectangle',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,200))
    elif len(approx) == 5:
        cv2.putText(img,'Pentagon',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,200))
    elif len(approx) == 10:
        cv2.putText(img,'STAR',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,200))
    else:
        cv2.putText(img,'Circle',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,200))
     
cv2.imshow('Shapes',img)
    
cv2.waitKey(0)
cv2.destroyAllWindows()
