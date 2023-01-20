from vidgear.gears import VideoGear
import cv2 as cv
import os
from difference import *
from tip import *

def startGame(boardPoints):

    centerOfBoard = [(boardPoints[0][0] + boardPoints[1][0]) // 2, (boardPoints[2][0] + boardPoints[3][0]) // 2]
    stream1 = VideoGear(source=0, logging=True).start() 
    stream2 = VideoGear(source=1, logging=True).start() 

    hitCount = 0
    frameCount = 0
    points = []

    if os.path.isfile('Images/previousA.jpg'):
        os.remove('Images/previousA.jpg')

    if os.path.isfile('Images/previousB.jpg'):
        os.remove('Images/previousB.jpg')

    while True:
        
        frameA = stream1.read()
        frameB = stream2.read()

        cv.imwrite('Images/emptyA.jpg', frameA)
        cv.imwrite('Images/emptyB.jpg', frameB)

        if frameA is None or frameB is None:
            break

        if not os.path.isfile('Images/previousA.jpg'):
            cv.imwrite('Images/previousA.jpg', frameA)
            cv.imwrite('Images/previousB.jpg', frameB)
        
        #cv.imshow("Output Frame1", frameA)
        #cv.imshow("Output Frame2", frameB)

        cv.imwrite('Images/currentA.jpg', frameA)
        cv.imwrite('Images/currentB.jpg', frameB)

        previousA = cv.imread('Images/previousA.jpg')
        previousB = cv.imread('Images/previousB.jpg')

        cntsA, boardContoursA, contourFoundA = findContour(previousA, frameA, 200, "A")
        cntsB, boardContoursB, contourFoundB = findContour(previousB, frameB, 200, "B")

        if contourFoundA or contourFoundB:
            frameCount += 1

            if frameCount == 3:
                cntsA, boardContoursA, contourFoundA = retrieveDartContour(previousA, frameA, 10, "A")
                cntsB, boardContoursB, contourFoundB = retrieveDartContour(previousB, frameB, 15, "B")

                tipA = findTip(boardContoursA, contourFoundA, "A")
                tipB = findTip(boardContoursB, contourFoundB, "B")

                diffA = centerOfBoard[0] - tipA[0]
                diffB = centerOfBoard[1] - tipB[0]

                ratioA = abs(34 / (boardPoints[1][0] - boardPoints[0][0])) 
                ratioB = abs(34 / (boardPoints[3][0] - boardPoints[2][0])) 
                point = calculatePoint(diffA, diffB, ratioA, ratioB) 

                points.append(point)

                hitCount += 1
                frameCount = 0

                cv.imwrite('Images/Hits/hit_' + str(hitCount) + '_A.jpg', boardContoursA)
                cv.imwrite('Images/Hits/hit_' + str(hitCount) + '_B.jpg', boardContoursB)

                cv.imwrite('Images/previousA.jpg', frameA)
                cv.imwrite('Images/previousB.jpg', frameB)
            
        if len(points) == 3:
            return points
        

    cv.destroyAllWindows()

    stream1.stop()
    stream2.stop()