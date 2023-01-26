import cv2 as cv
import matplotlib.pyplot as plt

# Reading the file
img = cv.imread("Resources/Photos/park.jpg")

# BGR to HSV
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# BGR to l.a.r
lar_img = cv.cvtColor(img, cv.COLOR_BGR2LAB)

# BGR to RGB
rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# BGR to Grayscale
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

"""
    Converting Formats back BGR
"""
gray_to_bgr = cv.cvtColor(gray_img, cv.COLOR_GRAY2BGR)
cv.imshow("Gray to BGR", gray_to_bgr)

hsv_to_bgr = cv.cvtColor(hsv_img, cv.COLOR_HSV2BGR)
cv.imshow("HSV to BGR", hsv_to_bgr)

# cv.imshow displays a new window
# Cat is the name of the window and img is the image to be read

# cv.imshow("Park", img)
# cv.imshow("Park HSV", hsv_img)
# cv.imshow("Park LAR", lar_img)
# cv.imshow("Park RGB", rgb_img)
# plt.imshow(rgb_img)
# plt.show()

cv.waitKey(0)