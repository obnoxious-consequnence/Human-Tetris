import numpy as np
import cv2
cap = cv2.VideoCapture(0)
seconds = 3

millis = seconds * 1000
while (millis > 0):
   # Capture frame-by-frame
    ret, frame = cap.read()
    millis = millis - 10
  # Display the resulting frame
    cv2.imshow('video recording', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
       #this method holds execution for 10 milliseconds, which is why we 
       #reduce millis by 10
        break

 #once the while loop breaks, write img
img_name = "example.jpg"
cv2.imwrite(img_name, frame)
print("{} written!".format(img_name))