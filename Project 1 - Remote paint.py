import cv2
import numpy as np

cap = cv2.VideoCapture(0)
myColors = [[37, 30, 38, 152, 255, 255], [0, 56, 29, 6, 255, 255]]    #blue #red # blacK = [25, 18,  0, 179, 255, 255]
colorValues = [[255,0,0],[0,0,255]]


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0,0,0,0
    for cnt in contours:
        # detect the area to remove noise
        area = cv2.contourArea(cnt)
        if area > 500:
            #cv2.drawContours(imgResult, cnt, -1, (0, 255, 0), 3)
            peri = cv2.arcLength(cnt, True)
            # return the corner points
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2, y

mypoints = []
def findcolor(img, myColors, colorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    for color in myColors:
        lower= np.array(color[0:3])
        upper = np.array(color[3:6])
        mask= cv2.inRange(imgHSV,lower,upper)
        # cv2.imshow(str(color[0]), mask)
        x, y = getContours(mask)
        if x != 0 and y != 0:
            #cv2.circle(imgResult, (x,y), 10, colorValues[count], cv2.FILLED)
            newPoint = [x,y, count]
            mypoints.append(newPoint)
        count += 1
    return mypoints


def draw(allpoints):
    for point in allpoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, colorValues[point[2]], cv2.FILLED)


while True:
    success, img = cap.read()
    imgResult = img.copy()
    allPoints = findcolor(img, myColors, colorValues)
    draw(allPoints)

    cv2.imshow("Res", imgResult)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break