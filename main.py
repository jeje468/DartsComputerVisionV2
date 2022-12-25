import numpy as np
import cv2 as cv

cap1 = cv.VideoCapture(0)
cap2 = cv.VideoCapture(1)

if not cap1.isOpened():
    print("Cannot open camera 1")
    exit()

if not cap2.isOpened():
    print("Cannot open camera 2")
    exit()

while True:

    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not ret1:
        print("Can't receive frame from camera 1.")
        break

    if not ret2:
        print("Can't receive frame from camera 2.")
        break

    cv.imshow('Camera 1', frame1)
    cv.imshow('Camera 2', frame2)

    if cv.waitKey(1) == ord('q'):
        break

cap1.release()
cap2.release()

cv.destroyAllWindows()