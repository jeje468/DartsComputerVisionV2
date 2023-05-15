import cv2 as cv
from difference import *
from calibrate import *
from tip import *
from difference import *
from gameplay import *
import sys

def takeEmptyImage():

    stream1 = VideoGear(source=2, logging=True).start() 
    stream2 = VideoGear(source=1, logging=True).start() 

    frameA = stream1.read()
    frameB = stream2.read()

    cv.imwrite("Images/Test/empty_A.jpg", frameA)
    cv.imwrite("Images/Test/empty_B.jpg", frameB)

    stream1.stop()
    stream2.stop()

areas = [(4393.5, 7833.0), (2201.0, 6642.0)]
tips = [(4, 201), (342, -104)]
    
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
    
    total_area_A = sum(c['area'] for c in contourFoundA)
    total_area_B = sum(c['area'] for c in contourFoundB)

    if total_area_B < 2000:
        areaDiff = abs(total_area_A - areas[0][0])
        minIdx = 0
        for i in range(1, len(areas)):
            if abs(total_area_A - areas[0][0]) < areaDiff:
                minIdx = i
        
        tipA = findTip(boardContoursA, contourFoundA, "A")

        diffA = centerOfBoard[0] - tipA[0]
        diffB = tips[minIdx][1]

        areas.append((sys.float_info.max, total_area_B))
    elif total_area_A < 2000:
        areaDiff = abs(total_area_B - areas[0][1])
        minIdx = 0
        for i in range(1, len(areas)):
            if abs(total_area_B - areas[0][1]) < areaDiff:
                minIdx = i
        
        tipB = findTip(boardContoursB, contourFoundB, "B")

        diffA = tips[minIdx][0]
        diffB = centerOfBoard[1] - tipB[0]        

        areas.append((sys.float_info.max, total_area_B))
    else:
        areas.append((total_area_A, total_area_B))

        tipA = findTip(boardContoursA, contourFoundA, "A")
        tipB = findTip(boardContoursB, contourFoundB, "B")

        diffA = centerOfBoard[0] - tipA[0]
        diffB = centerOfBoard[1] - tipB[0]
        
    cv.imwrite("Images/Test/hit_A.jpg", boardContoursA)
    cv.imwrite("Images/Test/hit_B.jpg", boardContoursB)

    tips.append((diffA, diffB))

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
