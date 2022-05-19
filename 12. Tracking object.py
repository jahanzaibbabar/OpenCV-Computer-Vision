import cv2

cap = cv2.VideoCapture(1)

success, img = cap.read()
cv2.waitKey(1000)
success, img = cap.read()
bbox = cv2.selectROI("Tracking", img, False)
tracker = cv2.TrackerMOSSE_create()
tracker.init(img, bbox)

def drawBox(img,bbox):
    x, y, w, h= int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 255), 3, 1)
    cv2.putText(img, "Tracking", (75, 70), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)


while True:
    timer = cv2.getTickCount()
    success, img = cap.read()

    success, bbox = tracker.update(img)

    if success:
        drawBox(img, bbox)
    else:
        cv2.putText(img, "Lost", (75, 70), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1)

    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

    cv2.rectangle(img, (60,30), (160, 80), (0, 255, 0), 2, 1)


    cv2.putText(img,"FPS: " + str(int(fps)), (75, 50), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 255), 1)
    cv2.imshow("Tracking", img)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
