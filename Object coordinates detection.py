### width of the image is x =480 % height is y =360

import cv2
import numpy as np


def empty(a):
    pass

def getLargestCnt(contours):
    largArea = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if largArea < area:
            largArea = area
    return largArea


frameWidth = 480
frameHeight = 360
cap = cv2.VideoCapture(0)

cap.set(3, frameWidth)
cap.set(4, frameHeight)

# creating trackbar
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640, 240)
cv2.createTrackbar("HUE Min", "HSV", 0, 179, empty)
cv2.createTrackbar("HUE Max", "HSV", 179, 179, empty)
cv2.createTrackbar("SAT Min", "HSV", 0, 255, empty)
cv2.createTrackbar("SAT Max", "HSV", 255, 255, empty)
cv2.createTrackbar("VALUE Min", "HSV", 0, 255, empty)
cv2.createTrackbar("VALUE Max", "HSV", 255, 255, empty)

while True:
    success, imgOriginal = cap.read()
    imgOriginal = cv2.resize(imgOriginal, (frameWidth, frameHeight))

    # blue HSV
    # blueLower = (57,  82, 166)
    # blueUpper = (134, 255, 255)

    blurred = cv2.GaussianBlur(imgOriginal, (11,11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    # access value of trackbar
    h_min = cv2.getTrackbarPos("HUE Min", "HSV")
    h_max = cv2.getTrackbarPos("HUE Max", "HSV")
    s_min = cv2.getTrackbarPos("SAT Min", "HSV")
    s_max = cv2.getTrackbarPos("SAT Max", "HSV")
    v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
    v_max = cv2.getTrackbarPos("VALUE Max", "HSV")

    # create the mask and AND it with original img
    # lower = np.array([h_min, s_min, v_min])
    # upper = np.array([h_max, s_max, v_max])
    lower = np.array([100, 156, 0])
    upper = np.array([120, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(imgOriginal,imgOriginal, mask=mask)

    # deleting noises which are in area of mask
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    center = None

    # get max contour
    try:
        c = max(contours, key=cv2.contourArea)
    except:
        continue
    #getLargestCnt(contours)

    rect = cv2.minAreaRect(c)

    ((x,y), (width, height), rotation) = rect
    s1 = f"x: {np.round(x)}, y: {np.round(y)}"
    s2 = f"width: {np.round(width)}, height: {np.round(height)}, rot: {np.round(rotation)}"

    # box
    box = cv2.boxPoints(rect)
    box = np.int64(box)

    # moment
    M = cv2.moments(c)
    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

    # point in center
    cv2.circle(imgOriginal, center, 5, (255, 0, 255), -1)

    # draw contour
    cv2.drawContours(imgOriginal, [box], 0, (0, 255, 255), 2)

    # print inform
    cv2.putText(imgOriginal, s1, (25, 20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 2)
    cv2.putText(imgOriginal, s2, (5, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 2)

    # converting mask to 3 dimentional
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    # stacking
    hStack = np.hstack([imgOriginal, mask, result])
    cv2.imshow("Output", hStack)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



