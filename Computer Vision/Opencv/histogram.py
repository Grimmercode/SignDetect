import cv2 as cv 
import matplotlib.pyplot as plt
import numpy as np 

img = cv.imread('maxresdefault.jpg')
cv.imshow('ss', img)

blank = np.zeros(img.shape[:2], dtype ='uint8')
circle = cv.circle(blank.copy(), ((img.shape[1]//2), (img.shape[0]//2)), 100, 255, -1)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grau', gray)

mask = cv.bitwise_and(gray,gray,mask=circle)
cv.imshow('mask', mask)


gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256] )

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

cv.waitKey(0)