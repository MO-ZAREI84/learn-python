import cv2
import numpy as np
# این اسکریپت توسط چت جی پی تی و استفاده از مدل های هوش مصنوعی نوشته شده است
# خواندن ویدیو
cap = cv2.VideoCapture("video.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # تبدیل به تصویر خاکستری
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # کاهش نویز با فیلتر گوسی
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # تشخیص لبه‌ها با الگوریتم Canny
    edges = cv2.Canny(blurred, 50, 150)

    # پیدا کردن کانتورها
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)

        # بررسی مستطیلی بودن و ابعاد مناسب پلاک
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            aspect_ratio = w / float(h)

            if 2 < aspect_ratio < 5:  # بررسی نسبت ابعاد معمولی پلاک
                plate = frame[y:y+h, x:x+w]

                # ذخیره تصویر پلاک برای پردازش بعدی
                cv2.imwrite("plate.jpg", plate)

                # رسم مستطیل دور پلاک
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # نمایش تصویر پردازش‌شده
    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
