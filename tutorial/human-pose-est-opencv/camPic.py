import numpy as np
import cv2
cap = cv2.VideoCapture(0)
seconds = 4

millis = seconds * 1000
while (millis > 1000):
   # Capture frame-by-frame
    ret, frame = cap.read()
    millis = millis - 10
  # Display the resulting frame
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontColor = (0, 0, 255)

    frame_width = frame.shape[1]
    frame_height = frame.shape[0]
  
    cv2.putText(frame, str(int(millis / 1000)), (int(frame_width / 2), 20), font, 0.6, fontColor, 1, cv2.LINE_AA)
    cv2.putText(frame, 'T-Pose', (20, 20), font, 0.6, fontColor, 1, cv2.LINE_AA)
    cv2.putText(frame, 'Score: ', (20, 50), font, 0.6, fontColor, 1, cv2.LINE_AA)
    
    cv2.imshow('video recording', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
       #this method holds execution for 10 milliseconds, which is why we 
       #reduce millis by 10
        break

 #once the while loop breaks, write img
img_name = "example.jpg"
cv2.imwrite(img_name, frame)
print("{} written!".format(img_name))

# print('width:', frame.shape[1])
# print('height:', frame.shape[0])