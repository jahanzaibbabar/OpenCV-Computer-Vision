import cv2
import numpy as np

counter = 0
points = np.zeros((4, 2), int)


def mousePoints(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        global counter
        points[counter] = x, y
        counter = counter + 1
        print(points)


img = cv2.imread("Resources/pic1.jpg")
# cap = cv2.VideoCapture(0)
# sucess,img = cap.read()
while True:
    if counter == 4:
        width, height = 250, 300
        pts1 = np.float32([points[0], points[1], points[2], points[3]])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgoutput = cv2.warpPerspective(img, matrix, (width, height))
        cv2.imshow("img Output", imgoutput)
        break

    for x in range(0, 4):
        cv2.circle(img, (int(points[x][0]), int(points[x][1])), 5, (0, 0, 255), cv2.FILLED)

    cv2.imshow("img", img)
    cv2.setMouseCallback("img", mousePoints)
    cv2.waitKey(1)

cv2.waitKey(0)
