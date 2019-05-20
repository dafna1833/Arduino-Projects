import numpy as np
import cv2

img = cv2.imread("example.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)

edge = cv2.Canny(gray, 10, 250)
cv2.imshow('here', edge)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(edge, cv2.MORPH_CLOSE, kernel)

counter, hierarchy = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
pts2 = np.float32([[0, 0], [0, 180], [120, 180], [120, 0]])
total = 0

for c in counter:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)

    if len(approx) == 4:
        cv2.drawContours(img, [approx], -1, (0, 255, 0), 4)
        total = total + 1
        pts1 = np.float32([approx])
        a = pts1[0][0][0][0]
        b = pts1[0][0][0][1]
        c = pts1[0][1][0][0]
        d = pts1[0][1][0][1]
        e = pts1[0][2][0][0]
        f = pts1[0][2][0][1]
        g = pts1[0][3][0][0]
        h = pts1[0][3][0][1]
        array = np.float32([[a, b], [c, d], [e, f], [g, h]])
        M = cv2.getPerspectiveTransform(array, pts2)
        new = cv2.warpPerspective(img, M, (120,180))
        cv2.imshow("new", new)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.DestroyWindow("new")
        print("This is one contour")
        print(approx)

print ('I found %d books in that image' % total)
cv2.imshow("Output", img)
cv2.waitKey(0)
