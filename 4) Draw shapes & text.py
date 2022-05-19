import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

# color
img[:] = 0, 255, 255

# Draw line
cv2.line(img, (0, 0), (100, 100), (255, 0, 0), 3)
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 0, 250), 1)

# my own trying to draw dot in center
width, height = img.shape[1], img.shape[0]
x = int(width / 2)
y = int(height / 2)
cv2.line(img, (x,y), (x,y), (0, 250, 0), 5)

#rectangle
cv2.rectangle(img, (200,100), (400,200), (0,250,0),2)

#circle
cv2.circle(img, (100,400),50, (0,0,250),cv2.FILLED)

#text
cv2.putText(img,"Draw Shapes", (120,50),cv2.FONT_HERSHEY_COMPLEX,1, (0, 0, 0),1)


cv2.imshow("Img", img)

cv2.waitKey(0)
