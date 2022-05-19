import cv2

# img = cv2.imread("Resources/pic.jpg")
#
# cv2.imshow("my_pic", img)
# cv2.waitKey(0)

frameWidth = 680
frameHeight = 480
cap = cv2.VideoCapture("Resources/video.mp4")
cap.set(3, frameWidth)
cap.set(4, frameHeight)


while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


