import cv2
import numpy as np 

img = cv2.imread(img_to_resize)

print('Original Dimensions : ',img.shape)
 
dim = (x, y)
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)

img_name = 'resized_0{}'.format(i)
cv2.imwrite(img_name, resized)
