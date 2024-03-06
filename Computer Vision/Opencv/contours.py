import cv2 as cv 
import numpy as np

img = cv.imread('ss.png')
cv.imshow('RGB', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# blur = cv.GaussianBlur(gray, (1,1), cv.BORDER_DEFAULT)
# cv.imshow('Blured', blur)

canny = cv.Canny(img, 125, 175)
cv.imshow('canny edge', canny)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours found !')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours drawn', blank)
cv.waitKey(0)
