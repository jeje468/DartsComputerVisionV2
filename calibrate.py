from tkinter import *
from vidgear.gears import VideoGear
import cv2 as cv
from difference import *
from tip import *
from gameplay import *

idx = 0

def takePhoto():
    stream0 = VideoGear(source=0, logging=True).start() 
    stream1 = VideoGear(source=1, logging=True).start() 

    global idx
    if idx < 3:
        calibrationImage = stream0.read()
    else:
        calibrationImage = stream1.read()

    #calibrationImage = cv.undistort(calibrationImage, mtx, dist, None, newcameramtx)
    
    cv.imwrite('Images/Calibration/calibration_' + str(idx) + '.jpg', calibrationImage)
    idx += 1

    stream0.stop()
    stream1.stop()

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

    leftPoint = findTip(boardContoursALeft, contourFoundALeft, "A")
    cv.circle(boardContoursALeft, (leftPoint[0], leftPoint[1]), 3, (0, 255, 0), -1)
    cv.imwrite("Images/CalibrationTip/left.jpg", boardContoursALeft)

    rightPoint = findTip(boardContoursARight, contourFoundARight, "A")
    cv.circle(boardContoursARight, (rightPoint[0], rightPoint[1]), 3, (0, 255, 0), -1)
    cv.imwrite("Images/CalibrationTip/right.jpg", boardContoursARight)
    
    topPoint = findTip(boardContoursBTop, contourFoundBTop, "B")
    cv.circle(boardContoursBTop, (topPoint[0], topPoint[1]), 3, (0, 255, 0), -1)
    cv.imwrite("Images/CalibrationTip/top.jpg", boardContoursBTop)

    bottomPoint = findTip(boardContoursBBottom, contourFoundBBottom, "B")
    cv.circle(boardContoursBBottom, (bottomPoint[0], bottomPoint[1]), 3, (0, 255, 0), -1)
    cv.imwrite("Images/CalibrationTip/bottom.jpg", boardContoursBBottom)

    cv.destroyAllWindows()

    return [leftPoint, rightPoint, topPoint, bottomPoint]



# master = Tk()

# Button(master, text='Take calibration photo', command=takePhoto).pack()
# Button(master, text='Finish calibration', command=calibrate).pack()

# stream1 = VideoGear(source=0, logging=True).start() 
# stream2 = VideoGear(source=1, logging=True).start() 

# while True:
    
#     frameA = stream1.read()
#     frameB = stream2.read()

#     if frameA is None or frameB is None:
#         break
    
#     cv.line(frameA, (int(frameA.shape[1] / 2), 0), (int(frameA.shape[1] / 2), int(frameA.shape[0])), [0, 255, 0], 3)
#     cv.line(frameB, (int(frameB.shape[1] / 2), 0), (int(frameB.shape[1] / 2), int(frameB.shape[0])), [0, 255, 0], 3)
    
#     cv.imshow("Output Frame1", frameA)
#     cv.imshow("Output Frame2", frameB)

#     key = cv.waitKey(1) & 0xFF
#     if key == ord("q"):
#         break

# cv.destroyAllWindows()

# stream1.stop()
# stream2.stop()

# master.mainloop()