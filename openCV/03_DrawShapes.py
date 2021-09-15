import cv2 as cv
import numpy as np
# Get a blank image
blank_img = np.zeros((512, 512, 3), np.uint8)

# Changing Bakground of a Blannk Image
blank_img[:] = (0, 255, 0)

# Draw a line
cv.line(blank_img, (0, 0), (511, 511), (255, 0, 0), 5)

# Draw a rectangle
cv.rectangle(blank_img, (384, 0), (510, 128), (0, 0, 0), 3)

# Draw a circle
cv.circle(blank_img, (447, 63), 63, (0, 0, 255), -1)

# Write text on image
cv.putText(blank_img, 'OpenCV', (10, 500), cv.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 2, cv.LINE_AA)

cv.imshow('Image',blank_img)
cv.waitKey(0)