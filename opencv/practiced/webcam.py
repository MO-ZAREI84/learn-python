import cv2
import numpy as np

# تنظیمات دوربین
width, height = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

# رنگ موردنظر در HSV
myColor = [(160, 120, 0), (179, 255, 255)]
myPoints = []  # لیست نقاط شناسایی‌شده

def findColor(img, myColor):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array(myColor[0])
    upper = np.array(myColor[1])
    mask = cv2.inRange(imgHSV, lower, upper)
    x, y = getContours(mask)
    if x != 0 and y != 0:
        cv2.circle(img, (x, y), 15, (255, 0, 0), cv2.FILLED)
        return [x, y]
    return None  # اگر نقطه‌ای پیدا نشد، مقدار None برگردان

def getContours(img):
    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x + (w // 2), y

def drawMyPoints(points, img):
    for point in points:
        cv2.circle(img, (point[0], point[1]), 15, (255, 0, 0), cv2.FILLED)  # رنگ آبی

while True:
    success, img = cap.read()
    imgResult = img.copy()
    
    # پیدا کردن رنگ
    newPoint = findColor(img, myColor)
    if newPoint is not None:
        myPoints.append(newPoint)  # فقط نقاط معتبر اضافه شوند
    
    # رسم نقاط پیدا شده
    if len(myPoints):
        drawMyPoints(myPoints, imgResult)
    
    cv2.imshow("Frame", imgResult)

    # خروج با فشردن 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
