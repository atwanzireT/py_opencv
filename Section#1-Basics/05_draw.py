import cv2 as cv
import numpy as np

blank = np.zeros((500, 500), dtype='uint8')
# Reading the file
img = cv.imread("Resources/Photos/cat2.jpg")

# Paint the image a certain color
# img[200:300, 300:400] = 255, 0, 0

# Draw a Rectangle
cv.rectangle(img, (0, 0), (255, 255), (0, 255, 0),  thickness=2)

# Draw a Circle
cv.circle(img, (255, 255), 50, (0, 0, 255), thickness=1)

# Put Text
cv.putText(img, "Hello", (255, 255), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 255), thickness=2)

# cv.imshow("Blank", blank)
cv.imshow("Cat Green",img)
cv.waitKey(0)