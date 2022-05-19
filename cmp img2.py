import cv2
import numpy as np
import imutils

#get the images you want to compare.
original = cv2.imread("Resources/1.jpg")
duplicate = cv2.imread("Resources/3.jpg")


# ######################
hsv = cv2.cvtColor(duplicate, cv2.COLOR_BGR2HSV)

lower_range = np.array([160,  52,  29])
upper_range = np.array([167, 247, 255])

mask = cv2.inRange(hsv, lower_range, upper_range)
duplicate = cv2.bitwise_xor(duplicate, duplicate, mask=mask)

# cv2.imshow('image', img)
#result = cv2.resize(result, (900, 500))
#cv2.imshow('mask', duplicate)


#################################=

# Store the image shape into variable
ori_shape = original.shape[:2]
dup_shape = duplicate.shape[:2]

# TEST 1: Based on shape of image
if ori_shape == dup_shape:
    print("Image size is same")
else:
    print("Image is different in size")

# TEST 1: Based on shape of image
if ori_shape == dup_shape:
    print("Image size is same")

    # Extract the difference of color element between two image
    difference = cv2.subtract(original, duplicate)
    #print(difference)
    b, g, r = cv2.split(difference)
    print(r)

# TEST 1: Based on shape of image
if ori_shape == dup_shape:
    # ...

    # TEST 2: Based on color of image
    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        print("The color is equal")
    else:
        print('The color of image is different')
        difference = cv2.resize(difference, (900,500))
        cv2.imshow('Difference', difference)
        #cv2.imshow('img', duplicate)
        cv2.waitKey(0)

else:
  pass