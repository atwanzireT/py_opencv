import cv2 as cv

# Reading the file
img = cv.imread("Resources/Photos/park.jpg")

# Averaging
average = cv.blur(img, (3, 3))

# GaussianBlur
gaus = cv.GaussianBlur(img, (7, 7), 0)

# Median blur
median_blur = cv.medianBlur(img, 3)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)

# cv.imshow displays a new window 
# Cat is the name of the window and img is the image to be read
cv.imshow("Average Blur", average)
cv.imshow("Gaussian Blur", gaus)
cv.imshow("Median Blur", median_blur)
cv.imshow('Bilateral', bilateral)
cv.waitKey(0)