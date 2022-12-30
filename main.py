from tkinter import *
from vidgear.gears import VideoGear
import cv2 as cv
from difference import *

stream0 = VideoGear(source=0, logging=True).start() 
stream1 = VideoGear(source=1, logging=True).start() 
idx = 0

def takePhoto():
    global idx
    if idx < 3:
        calibrationImage = stream0.read()
    else:
        calibrationImage = stream1.read()
    
    cv.imwrite('Images/Calibration/calibration_' + str(idx) + '.jpg', calibrationImage)
    idx += 1

def calibrate():

    cameraAEmpty = cv.imread('Images/Calibration/calibration_0.jpg')
    cameraALeft = cv.imread('Images/Calibration/calibration_1.jpg')
    cameraARight = cv.imread('Images/Calibration/calibration_2.jpg')

    cameraBEmpty = cv.imread('Images/Calibration/calibration_3.jpg')
    cameraBTop = cv.imread('Images/Calibration/calibration_4.jpg')
    cameraBBottom = cv.imread('Images/Calibration/calibration_5.jpg')

    cntsALeft, boardContoursALeft, contourFoundALeft = retrieveDartContour(cameraAEmpty, cameraALeft, 10, "A")
    cntsARight, boardContoursARight, contourFoundARight = retrieveDartContour(cameraAEmpty, cameraARight, 10, "A")

    cntsBTop, boardContoursBTop, contourFoundBTop = retrieveDartContour(cameraBEmpty, cameraBTop, 20, "B")
    cntsBBottom, boardContoursBBottom, contourFoundBBottom = retrieveDartContour(cameraBEmpty, cameraBBottom, 20, "B")

    cv.imshow('A left', boardContoursALeft)
    cv.imshow('A right', boardContoursARight)
    cv.imshow('B top', boardContoursBTop)
    cv.imshow('B bottom', boardContoursBBottom)

    cv.waitKey(0)


master = Tk()

Button(master, text='Take calibration photo', command=takePhoto).pack()
Button(master, text='Finish calibration', command=calibrate).pack()


master.mainloop()