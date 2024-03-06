import cv2 as cv


img = cv.imread('maxresdefault.jpg')
cv.imshow('ss', img)

def rescaleFrame(frame, scale=0.75):  #images,videos,live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)


    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

cv.waitKey(0)

# capture = cv.VideoCapture('videoplayback.mp4')

# while True:
#     isTrue, frame = capture.read()

#     frame_resized =  rescaleFrame(frame, scale=.2)

#     cv.imshow('Video', frame)
#     cv.imshow('Video Resized', frame_resized)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()