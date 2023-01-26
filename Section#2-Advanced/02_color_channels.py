import cv2 as cv
import numpy as np

# Reading the file
img = cv.imread("Resources/Photos/park.jpg")
blank = np.zeros(img.shape[:2], dtype='uint8')

# Split Merge
b, g, r = cv.split(img)

# Displaying Different colors
# cv.imshow("Blue", b)
# cv.imshow("Green", g)
# cv.imshow("Red", r)

# Merging the Color Channels together
merged_img = cv.merge([b,g,r])
blue_img = cv.merge([b, blank, blank])
green_img = cv.merge([blank, g, blank])
red_img = cv.merge([blank, blank, r])

cv.imshow("Merged Image", merged_img)
cv.imshow("Blue Img", blue_img)
cv.imshow("Green Img", green_img)
cv.imshow("Red Img", red_img)

# cv.imshow displays a new window
# Cat is the name of the window and img is the image to be read
# cv.imshow("Cat", img)

cv.waitKey(0)