import cv2

ankit=cv2.imread('lena.jpg',1)

print(ankit)

cv2.imshow('image',ankit)#image is the window name that will open the image
k = cv2.waitKey(0) & 0xFF #In the documentation, it is written to use this mask 0xFF.

# When ESC key is pressed then close the window
if k==27: #ESC key has the value 27
    cv2.destroyAllWindows()

# When s key is pressed then save the image file
elif k==ord('s'): #ord is builtin function takes one argument
    #When 's' key is pressed write an image to the file
    cv2.imwrite('lena_copy.png',ankit)
