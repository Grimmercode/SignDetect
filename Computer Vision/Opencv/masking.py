import cv2 as cv 
import numpy as np 

img = cv.imread('ss.png')
cv.imshow('RGB', img)

blank = np.zeros(img.shape[:2], dtype ='uint8')
cv.imshow('Blank', blank)

rectangle = cv.rectangle(blank.copy(), (800,100), (500,800), 255, -1)
circle = cv.circle(blank.copy(), ((img.shape[1]//2), (img.shape[0]//2)), 300, 255, -1)

new_shape = cv.bitwise_xor(rectangle,circle)
cv.imshow('new', new_shape)

masked = cv.bitwise_or(img,img,mask=new_shape)
cv.imshow('masked',masked)


cv.waitKey(0)