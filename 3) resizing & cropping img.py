import cv2

##cropping == img[height, width]
##resizing ==resize(img, width, height)

width, hiegh = 400, 500
img = cv2.imread("Resources/pic.jpg")
print(img.shape)
#resize
ResizedImg = cv2.resize(img, (width, hiegh))

#Crop
CropedImg =img[0:600,0:720]
print(ResizedImg.shape)
CropedResizedImg = ResizedImg[0:350, 0:400]

#resizing croped img to original shape
ResizeCropedImg = cv2.resize(CropedImg, (img.shape[1],img.shape[0]))

#croping img from middle and resize it
CropedMidleImg =            img[100:750, 100:600]


# cv2.imshow("Image", img)
cv2.imshow("Resized Image", ResizedImg)
# cv2.imshow("Cropped Image", CropedImg)
# cv2.imshow("Cropped Resized Image", CropedResizedImg)
# cv2.imshow("Resize Cropped Image", ResizeCropedImg)
cv2.imshow("CropedMidleImg Image", CropedMidleImg)



cv2.waitKey(0)
