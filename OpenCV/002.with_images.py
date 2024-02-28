import cv2

ankit=cv2.imread('lena.jpg',0)

# 2nd argument is a flag 
# flags: 0-grayscale, 1-color, -1-unchanged image

print(ankit)

cv2.imshow('image',ankit)   #image is the window name that will open the image
cv2.waitKey(5000)           #show the image for 5 seconds. Put 0 if don't want to close automatically.
cv2.destroyAllWindows()     #close all the windows that will open
