import cv2
import numpy as np

img = np.zeros((500,500,3) , np.uint8)

cv2.line(img, (0,0) , (500,500) , (0,255,0) , 2)
cv2.rectangle(img, (0,0) , (100,100) ,(0,0,255),3)
cv2.putText(img,"Hello opencv",(100,200),cv2.FONT_HERSHEY_COMPLEX, 2,(255,0,0), 1)

cv2.imshow("black image", img)

cv2.waitKey(5000)