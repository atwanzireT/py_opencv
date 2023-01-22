import cv2 as cv

# Reading the file
img = cv.imread("Resources/Photos/cat.jpg")

# cv.imshow displays a new window
# Cat is the name of the window and img is the image to be read
cv.imshow("Cat", img)

cv.waitKey(0)