import cv2
import time

###############################
frameWidth = 640
frameHeight = 480
path = 'Resources\haarcascades\haarcascade_russian_plate_number.xml'
minArea = 500
color = (255, 0, 255)

###############################
img = cv2.imread("Resources/a.jpg")
img = cv2.resize(img, (800,400))
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)
# cap.set(10, 150)
count = 1

nPlatecascade = cv2.CascadeClassifier(path)
while True:
    # success, img= cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlate = nPlatecascade.detectMultiScale(imgGray, 1.1,4)
    print("Total Number Plate Detected: " + str(len(numberPlate)))
    print(numberPlate)
    for x in list(range(len(numberPlate))):
        for (x,y,w,h) in [numberPlate[x]]:
            area = w*h
            if area > minArea:
                cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
                cv2.putText(img,"Number Plate", (x, y-5), cv2.FONT_HERSHEY_COMPLEX,0.7,
                            (0,250,0),)

                nPlateImg = img[y:y+h, x:x+w]
                cv2.imshow("Number Plate"+str(x), nPlateImg)

    cv2.imshow("Result", img)


    if cv2.waitKey(100000) & 0xff == ord('s'):
        nowTime = time.time()
        cv2.imwrite("Resources/Scanned/NoPlate_"+ str(nowTime) + ".jpg", nPlateImg)
        cv2.rectangle(img,(0,200), (640,300),(0,200, 0), cv2.FILLED)
        cv2.putText(img,'Image Saved', (150, 250),cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0, 255),1)
        cv2.imshow("Result", img)
        cv2.waitKey(1000)
        count += 1