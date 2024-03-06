import cv2 as cv 
import numpy as np 

video = cv.VideoCapture(0)
haar_cascade = cv.CascadeClassifier('haar_face.xml')

while True:
    success, img = video.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
    
    for (x,y,w,h) in faces_rect:
        cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

    cv.imshow('cam', img)

    cv.waitKey(1)
