import cv2 as cv 
# import matplotlib.pyplot as plt
import numpy as np 

img = cv.imread('munich.jpg')
#cv.imshow('ss', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('gray', gray)

#laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplacian', lap)

#sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

combined_sobel = cv.bitwise_or(sobelx,sobely)

cv.imshow('sobel X', sobelx)
cv.imshow('sobel Y', sobely)
cv.imshow('sobel X Y', combined_sobel)

canny = cv.Canny(gray, 150, 175)
cv.imshow('canny', canny)
cv.waitKey(0)