import cv2 as cv

img = cv.imread('yotsuba.png')
# cv.imshow('RGB', img)
def rescaleFrame(frame, scale=0.50):  #images,videos,live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)


    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized = rescaleFrame(img)
cv.imshow('Yots', resized)

gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow('grey', gray)

blur = cv.GaussianBlur(resized, (5,5), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('canny', canny)

dilated = cv.dilate(canny, (7,7), iterations=1)
cv.imshow('dilated', dilated)

eroded = cv.erode(dilated, (3,3),  iterations=1)
cv.imshow('eroded', eroded)

reimage = cv.resize(resized, (200,300), interpolation=cv.INTER_CUBIC)
cv.imshow('reimg', reimage)

cropped = resized[100:200, 100:300]
cv.imshow('cropped', cropped)

cv.waitKey(0)
