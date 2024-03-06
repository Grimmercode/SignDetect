import cv2 as cv 
import matplotlib.pyplot as plt

img = cv.imread('ss.png')
cv.imshow('RGB', img)

# plt.imshow(img)
# plt.show()

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# plt.imshow(rgb)
# plt.show()

#hsv to bgr 
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsv2bgr', hsv_bgr)

#lab to bgr
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('lab2bgr', lab_bgr)

cv.waitKey(0)