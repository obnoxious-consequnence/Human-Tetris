import cv2

img = cv2.imread("tpose.jpg")
crop_img = img[y:y+h, x:x+w]
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)