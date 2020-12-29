from matplotlib import pyplot as plt
import cv2
import numpy as np

def func(x):
    pass

cv2.namedWindow('Tracking')
img= cv2.imread('messi.jpg',0)

cv2.createTrackbar('TH1','Tracking',0,255,func)
cv2.createTrackbar('TH2','Tracking',0,255,func)
while True:
    frame=cv2.imread('messi.jpg')
    th1=cv2.getTrackbarPos('TH1','Tracking')
    th2=cv2.getTrackbarPos('TH2','Tracking')
    edges=cv2.Canny(frame,th1,th2)
    cv2.imshow('frame',frame)
    cv2.imshow('CANNEY',edges)
    key=cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyAllWindows()
'''canny=cv2.Canny(img,100,200)
titles=['image','canny']
images=[img,canny]

for i in range(2):
    plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()'''


