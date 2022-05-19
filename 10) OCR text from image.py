import cv2
import pytesseract

img = cv2.imread(r"Resources\dummy_text1.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
pytesseract.pytesseract.pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
print(pytesseract.image_to_string(img))

# # dectecting charcters
# hImg, wImg,_ = img.shape
# #config = r"--oem 3 --psm 6 outputbase digits"
# boxes = pytesseract.image_to_boxes(img) #,config=config)
# #print(boxes)
# for b in boxes.splitlines():
#     b = b.split(' ')
#     #print(b)
#     x,y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
#     cv2.rectangle(img, (x,hImg-y), (w, hImg-h), (0,0, 255), 1)
#     cv2.putText(img, b[0], (x, hImg-y+15), cv2.FONT_HERSHEY_PLAIN,1,(25,25,255), 1)

# Dectecting words
hImg, wImg,_ = img.shape
# this line add configurations for only output digits
# config = r"--oem 3 --psm 6 outputbase digits"
boxes = pytesseract.image_to_data(img)#, config=config)
print(boxes)
for x,b in enumerate(boxes.splitlines()):
    if x != 0:
        b = b.split()
        if len(b)==12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x,y), (w+x, h+y), (0,0, 255), 1)
            cv2.putText(img, b[11], (x, y-2), cv2.FONT_HERSHEY_PLAIN, 1, (25, 25, 255), 1)



# img = cv2.resize(img,(920,580))
cv2.imshow("img", img)
cv2.waitKey(0)