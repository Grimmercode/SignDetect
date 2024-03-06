import cv2 as cv
import numpy as np 
from pyzbar.pyzbar import decode

video = cv.VideoCapture(0)

while True:
    success, img = video.read()
    
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1,1,2))
        cv.polylines(img, [pts], True, (255,0,255), 3)
        pts2 = barcode.rect
        cv.putText(img, myData, (pts2[0],pts2[1]), cv.FONT_HERSHEY_SIMPLEX, 0.9, (255,0,0), 2)

  
    cv.imshow('cam', img)

    cv.waitKey(1)

