import cv2 as cv  

img = cv.imread('ss.png')
cv.imshow('img', img)

#averaging
average = cv.blur(img, (3,3))
cv.imshow('Avarage Blur', average)

#gaussian blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gauss blur', gauss)

#median blur
median = cv.medianBlur(img, 3)
cv.imshow('median', median)

#bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('bileteral', bilateral)

cv.waitKey(0)
