import cv2

cap = cv2.VideoCapture(0);
fourcc = cv2.VideoWriter_fourcc(*'XVID') #these are 4 digits code to specify Video Codec
out = cv2.VideoWriter('output.mp4',fourcc,20.0,(640,480)); #VideoWriter class 1st argument is output file name, 2nd is fourcc code, 3rd is frame rate, 4th is size of the video

while(True): #cap.isOpened() will return TRUE if the file path or video source is correct
    ret, frame = cap.read()
    if ret == True: #If the frame is available or not
        gray=cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)#change color to graycale #FIRST ARGUMENT is the frame source and SECOND is the conversion that we want to do 
        cv2.imshow('frame',gray)

        out.write(frame) #out is the instance of videowriter
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()