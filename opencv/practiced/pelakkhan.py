import cv2
import numpy as np
import os

# بارگذاری مدل تشخیص پلاک
platCascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
minArea = 200

# بررسی و ساخت دایرکتوری ذخیره تصاویر
if not os.path.exists("scaned"):
    os.makedirs("scaned")

# بارگذاری ویدیو
cap = cv2.VideoCapture('video12.mp4')
cap.set(3, 640)
cap.set(4, 480)

count = 0

while True:
    success, img = cap.read()
    
    if not success:  # بررسی اگر ویدیو تمام شده باشد
        break

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberplates = platCascade.detectMultiScale(imgGray, 1.1, 10)

    plates = []  # لیست ذخیره پلاک‌ها

    for (x, y, w, h) in numberplates:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
        cv2.putText(img, "plate Detected", (x, y - 15), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 1)

        plates.append(img[y:y+h, x:x+w])  # ذخیره پلاک‌ها

    cv2.imshow("result", img)

    key = cv2.waitKey(1) & 0xFF  # افزایش زمان انتظار برای تشخیص بهتر کلیدها
    if key == ord('s'):
        if plates:  # اگر حداقل یک پلاک شناسایی شده بود
            for plate in plates:
                cv2.imwrite(f"scaned/{count}.jpg", plate)
                print(f"پلاک ذخیره شد: scaned/{count}.jpg")
                count += 1
        else:
            print("هیچ پلاکی برای ذخیره وجود ندارد!")

    if key == ord('q'):  # خروج با زدن دکمه 'q'
        break

cap.release()
cv2.destroyAllWindows()
