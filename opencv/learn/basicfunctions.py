import cv2
import numpy

img = cv2.imread(r"resources/lena.png")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBulur = cv2.GaussianBlur(imgGray, ksize=(7,7), sigmaX=0)
imgcanny = cv2.Canny(img, 150 , 200)

#white noise removal
kernel = numpy.ones((3,3) , numpy.uint8)
imgDilate = cv2.dilate(imgcanny, kernel , iterations=1)
imgErode = cv2.erode(imgDilate, kernel , iterations=1)

cv2.imshow("img",img)
cv2.imshow("imgGray", imgGray)
cv2.imshow("imgBulur",imgBulur)
cv2.imshow("imgCanny",imgcanny)
cv2.imshow("white noise removal", imgErode)

cv2.waitKey(0)