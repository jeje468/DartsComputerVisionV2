import cv2 as cv
from difference import *
from calibrate import *
from tip import *
from difference import *
from gameplay import *

def takeEmptyImage():

    stream1 = VideoGear(source=2, logging=True).start() 
    stream2 = VideoGear(source=1, logging=True).start() 

    frameA = stream1.read()
    frameB = stream2.read()

    cv.imwrite("Images/Test/empty_A.jpg", frameA)
    cv.imwrite("Images/Test/empty_B.jpg", frameB)

    stream1.stop()
    stream2.stop()
    
def test2():
    calibrationPoints = getCalibrationPoints()
    centerOfBoard = [(calibrationPoints[0][0] + calibrationPoints[1][0]) // 2, (calibrationPoints[2][0] + calibrationPoints[3][0]) // 2]

    stream1 = VideoGear(source=2, logging=True).start() 
    stream2 = VideoGear(source=1, logging=True).start() 

    emptyBoardA = cv.imread("Images/Test/empty_A.jpg")
    emptyBoardB = cv.imread("Images/Test/empty_B.jpg")

    frameA = stream1.read()
    frameB = stream2.read()
    
    stream1.stop()
    stream2.stop()
    
    cntsA, boardContoursA, contourFoundA = retrieveDartContour(emptyBoardA, frameA, 10, "A")
    cntsB, boardContoursB, contourFoundB = retrieveDartContour(emptyBoardB, frameB, 15, "B")
    
    cv.imwrite("Images/Test/hit_A.jpg", boardContoursA)
    cv.imwrite("Images/Test/hit_B.jpg", boardContoursB)

    tipA = findTip(boardContoursA, contourFoundA, "A")
    tipB = findTip(boardContoursB, contourFoundB, "B")

    diffA = centerOfBoard[0] - tipA[0]
    diffB = centerOfBoard[1] - tipB[0]

    ratioA = abs(34 / (calibrationPoints[1][0] - calibrationPoints[0][0])) 
    ratioB = abs(34 / (calibrationPoints[3][0] - calibrationPoints[2][0])) 
    point, isDouble = calculatePoint(diffA, diffB, ratioA, ratioB) 

    return point
    

# calibrationPoints = []

# with open('calibrationPoints.txt') as f:
#     lines = f.readlines()
#     for line in lines:
#         coordinates = line.rstrip('\n').split(",")
#         calibrationPoints.append((int(coordinates[0]), int(coordinates[1])))

# startGame(calibrationPoints, 1000)
