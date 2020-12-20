import cv2
cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'xvid')
out=cv2.VideoWriter('Output.avi',fourcc,20.0,(640,480))

while(cap.isOpened()) :
    ret, frame= cap.read()
    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out.write(frame)
        bhoora=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Window',bhoora)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
out.release()
cap.release()
cv2.destroyAllWindows()
