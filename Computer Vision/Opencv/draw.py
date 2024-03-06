import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8') 
#cv.imshow('blank', blank)

# img = cv.imread('maxresdefault.jpg')
# cv.imshow('SS', img)


# blank[200:300, 100:300] = 0,0,255 #colour
# cv.imshow('Red', blank)

# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,250,0), thickness=-1)
# cv.imshow('rect',blank)

# cv.circle(blank, (250,250), (100), (0,0,255), thickness=-1)
# cv.imshow('circle', blank) 

# cv.line(blank, (250,250), (500,500), (0,255,0), thickness=5)
# cv.imshow('line', blank)

cv.putText(blank, 'ALLAH', (220,260), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,255), thickness=2)
cv.imshow('text', blank)

cv.waitKey(0)