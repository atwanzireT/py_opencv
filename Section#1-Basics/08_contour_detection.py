import cv2 as cv
import numpy as np

img = cv.imread("Resources/Photos/cats.jpg")

# Blank Image
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

# Converting Image to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Converting Gray Image
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Threshold
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) 

# Getting Edges
canny = cv.Canny(img, 125, 175)

# Finding Contours
contours, hierarcy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

# Drawing Contours on the Image
cv.drawContours(blank, contours, -1, (0,0, 255), 1)


# View Image in the Frame
cv.imshow("Cat", img)
cv.imshow("Gray", gray)
cv.imshow("Thresh", thresh)
cv.imshow("Drawn Contours", blank)
cv.waitKey(0)