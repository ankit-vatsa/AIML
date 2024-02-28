import cv2

cap = cv2.VideoCapture(0);

#cap.isOpened() will return TRUE if the file path or video source is correct
print(cap.isOpened())
while(cap.isOpened()): #cap.isOpened() will return TRUE if the file path or video source is correct
    ret, frame = cap.read()

    gray=cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)#change color to graycale #FIRST ARGUMENT is the frame source and SECOND is the conversion that we want to do 
    cv2.imshow('frame',gray)

    #to get and print the height and width of the frame using the inbuilt functions
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindoqws()