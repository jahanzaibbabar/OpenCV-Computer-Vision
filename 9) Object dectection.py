import cv2
import numpy as np

# func to stack the output windows
def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


def getContours(img, imgContour):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        # detect the area to remove noise
        area = cv2.contourArea(cnt)
        areaMin = cv2.getTrackbarPos("Area", "Trackbarw")
        if area > areaMin:
            cv2.drawContours(imgContour, contours, -1, (0, 255, 0), 7)
            peri = cv2.arcLength(cnt, True)
            # return the corner points
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)

            x, y, w, h = cv2.boundingRect(approx)
            print(x,y)
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 0, 255), 5)
            cv2.putText(imgContour, "Points: " + str(len(approx)), (x + w + 20, y + 20), cv2.FONT_HERSHEY_COMPLEX,
                        0.7, (0, 0, 255), 1)
            cv2.putText(imgContour, "Area: " + str(int(area)), (x + w + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX,
                        0.7, (0, 0, 255), 1)

            # own code, to show box on sperate img
            cv2.rectangle(imgRes, (x, y), (x + w, y + h), (0, 0, 255), 5)
            cv2.putText(imgRes, "Points: " + str(len(approx)), (x + w + 20, y + 20), cv2.FONT_HERSHEY_COMPLEX,
                        0.7, (0, 0, 255), 1)
            cv2.putText(imgRes, "Area: " + str(int(area)), (x + w + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX,
                        0.7, (0, 0, 255), 1)


def empty(a):
    pass


frameWidth = 480
frameHeight = 360
cap = cv2.VideoCapture(0)

cap.set(3, frameWidth)
cap.set(4, frameHeight)

cv2.namedWindow("Trackbarw")
cv2.resizeWindow("Trackbarw", 640, 240)
cv2.createTrackbar("Threshold1", "Trackbarw", 40, 255, empty)
cv2.createTrackbar("Threshold2", "Trackbarw", 70, 255, empty)
cv2.createTrackbar("Area", "Trackbarw", 2000, 30000, empty)

while True:
    success, img = cap.read()
    imgContour = img#.copy()
    imgRes = img
    # # own code to resize windows
    # imgRes = cv2.resize(imgRes, (frameWidth, frameHeight))
    # img = cv2.resize(img, (frameWidth, frameHeight))
    # imgContour = cv2.resize(imgContour, (frameWidth, frameHeight))

    # gray the img to get useful more useful results ,and after blurit
    imgBlur = cv2.GaussianBlur(img, (7, 7), 1)
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)

    threshold1 = cv2.getTrackbarPos("Threshold1", "Trackbarw")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Trackbarw")
    # canny the img to get edges
    imgCanny = cv2.Canny(imgGray, threshold1, threshold2)
    # dilate the img to get perfect edges
    kernal = np.array((5, 5))
    imgDil = cv2.dilate(imgCanny, kernal, iterations=1)

    getContours(imgDil, imgContour)

    imgStack = stackImages(0.8, ([img, imgCanny, imgGray],
                                 [imgDil, imgRes, imgContour]))
    cv2.imshow("Result", imgStack)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()