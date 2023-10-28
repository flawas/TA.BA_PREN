import cv2
import numpy as np

cap = cv2.VideoCapture('*/train/3D-Builder-Example.mp4')

while True:
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([90, 60, 0])
    upper_blue = np.array([121, 255, 255])

    msk = cv2imRange(hsv, lower_blue, upper_blue)

    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for x in cnts:

        if area > 500:
            area = cv2.contourArea(x)

            cv2.drawContours(frame, [x], -1, (0, 255, 0), 3)

            M = cv2.moments(x)

            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            cv2.imshow("frame", frame)

    print("area is ...", area)
    print("centroid is at ...", cx, cy)

    k = cv2.waitKey(1000)
    if k == 27:
        break
