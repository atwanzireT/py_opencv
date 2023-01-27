import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# Reading the file
img = cv.imread("Resources/Photos/cats 2.jpg")

# Blank
blank = np.zeros(img.shape[:2], dtype="uint8")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

mask = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('Mask', masked)

# Grayscale Histo
gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256] )

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

# cv.imshow displays a new window
# Cat is the name of the window and img is the image to be read

# cv.imshow("Cat", img)

cv.waitKey(0)