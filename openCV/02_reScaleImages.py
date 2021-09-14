import cv2 as cv
img = cv.imread('Images/1.jpg')
cv.imshow('image', img)

#  Fumction to rescale Images by taking image and scale as an argument
def rescale_image(image, scale):
    width = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)
    dim = (width, height)
    resized = cv.resize(image, dim, interpolation=cv.INTER_AREA)
    return resized


#  Rescaling the image by 50%
cv.imshow('image', rescale_image(img, 0.5))
cv.waitKey(0)