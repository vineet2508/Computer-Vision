import cv2
import datetime
cap=cv2.VideoCapture(0)
#associative no. for height(CAP_PROP_FRAME_HEIGHT) is : 3
cap.set(3, 1208)
cap.set(4, 720)
print(cap.get(3))
print(cap.get(4))
while(cap.isOpened()):
    ret, frame=cap.read()
    if(ret==True):
        font=cv2.FONT_HERSHEY_SIMPLEX
        text='Width :' + str(cap.get(3)) + 'Height :' + str(cap.get(4))
        datet=str(datetime.datetime.now())
        frame=cv2.putText(frame,text,(10,50),font,2,(0,255,255),3,cv2.LINE_AA)
        frame=cv2.putText(frame,datet,(10,110),font,2,(0,255,0),3,cv2.LINE_AA)
        cv2.imshow('Window',frame)
        if(cv2.waitKey(1) & 0xFF == ord('q')):
           break
    else:
        break
cap.release()
cv2.destroyAllWindows()
           
