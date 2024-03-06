import cv2 as cv
import numpy as np 

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('rectangle', rectangle)
cv.imshow('circle', circle)

#bitwise AND
bitwise_and = cv.bitwise_and(circle,rectangle)
cv.imshow('wise', bitwise_and)

#bitwise or
bitwise_or = cv.bitwise_or(circle,rectangle)
cv.imshow('or', bitwise_or)

#bitwise xor
bitwise_xor = cv.bitwise_xor(circle,rectangle)
cv.imshow('xor', bitwise_xor)

#bitwise not
bitwise_not = cv.bitwise_not(rectangle,circle)
cv.imshow('not', bitwise_not)







cv.waitKey(0)