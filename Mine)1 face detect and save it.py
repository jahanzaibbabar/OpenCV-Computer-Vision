import cv2
import time
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

################################################################
pathCascade = 'E:\Mylife\Python\Python code\learning\LearnOpencv\Resources\haarcascades\haarcascade_frontalface_default.xml'  # PATH OF THE CASCADE
cameraNo = 1                       # CAMERA NUMBER
objectName = 'Face'       # OBJECT NAME TO DISPLAY
frameWidth = 640                     # DISPLAY WIDTH
frameHeight = 480                  # DISPLAY HEIGHT
color = (255,0,255)
minBlur = 500  # SMALLER VALUE MEANS MORE BLURRINESS PRESENT
frameNo = 10

driveFolder_id = '11PeKoGZDwwLbtSqhRLA_WaZdv29TxdTs'
pathLocalImgFolder = 'Resources\Face Detected'
#################################################################

# Login to Google Drive and create drive object
g_login = GoogleAuth()
g_login.LocalWebserverAuth()
drive = GoogleDrive(g_login)


cap = cv2.VideoCapture(cameraNo)
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)

def empty(a):
    pass

# CREATE TRACKBAR
cv2.namedWindow("Result")
cv2.resizeWindow("Result",frameWidth,frameHeight+100)
cv2.createTrackbar("Scale","Result",250,1000,empty)
cv2.createTrackbar("Neig","Result",7,50,empty)
cv2.createTrackbar("Min Area","Result",1000,100000,empty)
cv2.createTrackbar("Brightness","Result",180,255,empty)


def imgSave():
    nowTime = time.time()
    imgName = "Img_" + str(nowTime) + ".jpg"
    imgPath = pathLocalImgFolder + "\\" + imgName
    cv2.imwrite(imgPath, imgRoi)

    file_drive = drive.CreateFile({'title': imgName, 'mimeType': 'image/jpeg',
                                   'parents': [{'kind': 'drive#fileLink', 'id': driveFolder_id}]})
    file_drive.SetContentFile(imgPath)
    file_drive.Upload()
    print("The file: " + imgName + " has been uploaded")


# LOAD THE CLASSIFIERS DOWNLOADED
cascade = cv2.CascadeClassifier(pathCascade)
count = 0
while True:
    # SET CAMERA BRIGHTNESS FROM TRACKBAR VALUE
    cameraBrightness = cv2.getTrackbarPos("Brightness", "Result")
    cap.set(10, cameraBrightness)
    # GET CAMERA IMAGE AND CONVERT TO GRAYSCALE
    success, img = cap.read()
    imgWarn = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # DETECT THE OBJECT USING THE CASCADE
    scaleVal =1 + (cv2.getTrackbarPos("Scale", "Result") /1000)
    neig=cv2.getTrackbarPos("Neig", "Result")
    face = cascade.detectMultiScale(gray,scaleVal, neig)
    # DISPLAY THE DETECTED OBJECTS
    for (x,y,w,h) in face:
        area = w*h
        minArea = cv2.getTrackbarPos("Min Area", "Result")
        if area > minArea:
            cv2.rectangle(img,(x,y),(x+w,y+h),color,3)
            cv2.putText(img,objectName,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            imgRoi = img[y:y+h, x:x+w]
            cv2.imshow("Face", imgRoi)

            cv2.rectangle(imgWarn, (0, 200), (640, 300), (0, 200, 0), cv2.FILLED)
            cv2.putText(imgWarn, 'DON`T TOUCH MY LAPTOP', (150, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)
            cv2.putText(imgWarn, 'You Are Detected', (150, 290), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)
            cv2.imshow("Result", imgWarn)

            blur = cv2.Laplacian(imgRoi, cv2.CV_64F).var()
            if count % frameNo ==0 and blur > minBlur:
                imgSave()
            count +=1


    cv2.imshow("Result", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
         break