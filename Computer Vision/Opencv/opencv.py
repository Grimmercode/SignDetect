import cv2 as cv


#img = cv.imread('maxresdefault.jpg')
#cv.imshow('ss', img)


capture = cv.VideoCapture('videoplayback.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
