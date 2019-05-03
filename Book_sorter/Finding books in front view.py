import numpy as np
import cv2

img = cv2.imread("example.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)

edge = cv2.Canny(gray, 10, 250)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(edge, cv2.MORPH_CLOSE, kernel)

counter, hierarchy = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
total = 0

for c in counter:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)

    if len(approx) == 4:
        cv2.drawContours(img, [approx], -1, (0, 255, 0), 4)
        total = total + 1
        print(approx[0])

print ('I found %d books in that image' % total)
cv2.imshow("Output", img)
cv2.waitKey(0)
