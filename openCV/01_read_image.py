import cv2 as cv


img = cv.imread('Images/1.jpg')
cv.imshow('image', img)

video = cv.VideoCapture(0)
while True:
    check, frame = video.read()
    cv.imshow('video', frame)
    key = cv.waitKey(1)
    if key == ord('q'):
        break
video.release()
cv.destroyAllWindows()
cv.waitKey(0)