import cv2

vid = cv2.VideoCapture(r"resources/test_video.mp4")

while True:
    success, img = vid.read()
    n = cv2.resize(img , (320,240))
    cv2.imshow("Movie", img)
    if (cv2.waitKey(5)& 0xFF)== ord('q'):
       break
cv2.destroyAllWindows()
