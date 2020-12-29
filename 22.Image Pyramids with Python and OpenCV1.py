import cv2
import numpy as np
img= cv2.imread('lena.jpg')
lr1= cv2.pyrDown(img)
lr2=cv2.pyrDown(lr1)
hr2=cv2.pyrUp(lr2)
cv2.imshow('Original',img)
cv2.imshow('LR1',lr1)
cv2.imshow('LR2',lr2)
cv2.imshow('Hr',hr2)
cv2.waitKey(0)
cv2.destroyAllWindows()
