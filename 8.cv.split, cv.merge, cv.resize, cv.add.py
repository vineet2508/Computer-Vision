import numpy as np
import cv2
img=cv2.imread('messi.jpg')
img2=cv2.imread('lena.jpg')
print(img.shape)
print(img.size)
print(img.dtype)
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))

#face = img[163:238, 343:314]
#img[163:61,343:137] = face
face = img[280:340, 330:390]
img[273:333,100:160] = face

img=cv2.resize(img,(512,512))
img2=cv2.resize(img2,(512,512))
dst = cv2.addWeighted(img,.9,img2,.1,0)

cv2.imshow('RootWindow',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
