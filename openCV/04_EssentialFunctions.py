import cv2 as cv
import numpy as np

img = cv.imread('Images/1.jpg')

# Changing to Greyscale image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Greyscale', gray)

# Blurring the image
blur = cv.GaussianBlur(img, (5, 5), 0)
# cv.imshow('Blurred', blur)

# Finding the edges
edges = cv.Canny(blur, 90, 50)
# cv.imshow('Edges', edges)

# Dialating the image
dialated = cv.dilate(edges, (3,3), iterations=1)
# cv.imshow('Dialated', dialated)

# Eroding the image
eroded = cv.erode(dialated, (3,3), iterations=1)
# cv.imshow('Eroded', eroded)

# Resizing the image
resized = cv.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv.imshow('Resized', resized)

# Cropping the image
cropped = img[0:200, 0:200]
cv.imshow('Cropped', cropped)

cv.waitKey(0)