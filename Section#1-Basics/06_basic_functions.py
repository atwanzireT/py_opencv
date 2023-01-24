import cv2 as cv

# Reading the file
img = cv.imread("Resources/Photos/cats.jpg")

# Converting the image to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Bluring the Img
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)

# Edge Cascade
canny = cv.Canny(img, 125, 175)

# Ditaling the Image
ditaled = cv.dilate(canny, (3, 3), iterations=1)

# Eroding the Image
eroded = cv.erode(ditaled, (3,3), iterations=1)

# Resize Image
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)

# cropping the Image
cropped = img[50:200, 200:400]

# cv.imshow displays a new window
# Cat is the name of the window and img is the image to be read
cv.imshow("Cat", img)

# Gray Img
cv.imshow("GRAY", gray)

# Blur Img
cv.imshow("Blur", blur)

# Canny Img
cv.imshow("Canny", canny)

# Dilated Image
cv.imshow("Dilated", ditaled)

# Eroded Image
cv.imshow("Eroded", eroded)

# Cropped Img
cv.imshow("Croppped", cropped)

cv.waitKey(0)