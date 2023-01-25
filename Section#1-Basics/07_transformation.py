import cv2 as cv
import numpy as np

# Reading the file
img = cv.imread("Resources/Photos/lady.jpg")

# Translation
def translate(img, x, y):
    transmat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions =(img.shape[1], img.shape[0])
    return cv.warpAffine(img, transmat, dimensions) 

# Rotation
def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]

    if rotPoint == None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions) 

# Flipping the Image
flipped = cv.flip(img, -1)

translated =  translate(img, 100, 100)
rotated = rotate(img, 45)
# Displaying the Img
cv.imshow("Lady", img)
cv.imshow("Translated", translated)
cv.imshow("Rotated", rotated)
cv.imshow("Flipped", flipped)

cv.waitKey(0)