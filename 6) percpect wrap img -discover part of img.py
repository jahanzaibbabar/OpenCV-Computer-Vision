import cv2
import numpy as np

img = cv2.imread("Resources/pic1.jpg")

width, height = 250, 300
pts1 = np.float32([[123, 163], [188, 32], [364, 233], [418, 98]])
pts2 = np.float32([[0,0],[width,0], [0, height],[width, height]])
print(pts2)

matrix =cv2.getPerspectiveTransform(pts1, pts2)
imgoutput = cv2.warpPerspective(img, matrix, (width, height))

for x in range(0, 4):
    cv2.circle(img, (int(pts1[x][0]), int(pts1[x][1])), 5, (0, 0, 255), cv2.FILLED)

cv2.imshow("img", img)
cv2.imshow("img Output", imgoutput)

cv2.waitKey(0)
