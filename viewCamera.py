import cv2
#instantiate videocapture object (0 is for the default webcam)
cap = cv2.VideoCapture(0)

while(True):
    #read frame from video file
    ret, frame = cap.read()
    cv2.imshow('frame',frame)

    #if esc key pressed or no more video input
    if cv2.waitKey(1) & 0xFF == 27 or ret==False:
        break

# When everything done, release the capture

cv2.destroyAllWindows()
cap.release() 
