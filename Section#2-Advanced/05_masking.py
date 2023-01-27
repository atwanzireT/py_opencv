import cv2 as cv
import numpy as np

# Reading the file
img = cv.imread("Resources/Photos/cats.jpg")

# Blank Image
blank = np.zeros(img.shape[:2], dtype='uint8')
# cv.imshow('Blank Image', blank)

# Masking
mask = cv.circle(blank, (img.shape[1]//2 + 45, img.shape[0]//2), 100, 255, -1)
# cv.imshow("Mask", mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("Masked Image", masked)


# cv.imshow displays a new window
# Cat is the name of the window and img is the image to be read
cv.imshow("Cat", img)

cv.waitKey(0)