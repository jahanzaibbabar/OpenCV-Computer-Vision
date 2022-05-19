import cv2
import numpy

kernal = numpy.ones((5, 5), numpy.uint8)

path = "Resources/pic.jpg"
img = cv2.imread(path)

grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurImg = cv2.GaussianBlur(img, (5,5), 0)
cannyImg = cv2.Canny(img, 100,200)
imgdilate =cv2.dilate(cannyImg, kernal, iterations = 1)
imgEroded = cv2.erode(imgdilate, kernal, iterations=1)


# cv2.imshow("img", img)
# cv2.imshow("img2", grayimg)
# cv2.imshow("Blur Image", blurImg)
cv2.imshow("Canny Image", cannyImg)
cv2.imshow("dilate Image", imgdilate)
cv2.imshow("Erosion Image", imgEroded)

cv2.waitKey(0)




