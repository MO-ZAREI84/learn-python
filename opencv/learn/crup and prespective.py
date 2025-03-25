import cv2
import numpy as np

# بارگیری تصویر
img = cv2.imread(r"resources/cards.jpg")

# بررسی اینکه تصویر درست لود شده یا نه
if img is None:
    print("خطا: تصویر پیدا نشد! مسیر رو بررسی کن.")
    exit()

width = 164
height = 257

points1 = np.float32([[110,218], [291,186], [151,486], [354,442]])
points2 = np.float32([[0,0], [width,0], [0,height], [width,height]])

# محاسبه ماتریس تبدیل و اعمال پرسپکتیو
matrix = cv2.getPerspectiveTransform(points1, points2)
KingImage = cv2.warpPerspective(img, matrix, (width, height))

# نمایش تصاویر
cv2.imshow("All Cards", img)
cv2.imshow("King Card", KingImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
