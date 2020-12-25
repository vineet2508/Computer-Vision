import cv2
import numpy as np
img=cv2.imread('lena.jpg',1)
img=cv2.line(img,(0,0),(255,255),(0,223,0),10)
img=cv2.arrowedLine(img,(255,255),(510,510),(230,0,0),10)
img=cv2.rectangle(img,(0,110),(50,60),(0,0,220),7)
img=cv2.circle(img,(440,65),30,(123,12,123),6)
font=cv2.FONT_HERSHEY_SIMPLEX
img=cv2.putText(img,'VineetRajParashar',(10,150),font,2,(0,255,0),3,cv2.LINE_AA)
cv2.imshow('Window',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
