import cv2

img = cv2.imread(r"resources/lena.png")

if img is None:
    print("خطا: تصویر پیدا نشد! مسیر رو بررسی کن.")
else:
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
