from vidgear.gears import VideoGear
import cv2 as cv
import os
from difference import *

stream1 = VideoGear(source=0, logging=True).start() 
stream2 = VideoGear(source=1, logging=True).start() 

hitCount = 0
frameCount = 0

if os.path.isfile('Images/previousA.jpg'):
    os.remove('Images/previousA.jpg')

if os.path.isfile('Images/previousB.jpg'):
    os.remove('Images/previousB.jpg')

while True:
    
    frameA = stream1.read()
    frameB = stream2.read()

    if frameA is None or frameB is None:
        break

    if not os.path.isfile('Images/previousA.jpg'):
        cv.imwrite('Images/previousA.jpg', frameA)
        cv.imwrite('Images/previousB.jpg', frameB)
    
    cv.imshow("Output Frame1", frameA)
    cv.imshow("Output Frame2", frameB)

    cv.imwrite('Images/currentA.jpg', frameA)
    cv.imwrite('Images/currentB.jpg', frameB)

    previousA = cv.imread('Images/previousA.jpg')
    previousB = cv.imread('Images/previousB.jpg')

    cntsA, boardContoursA, contourFoundA = findContour(previousA, frameA, 200, "A")
    cntsB, boardContoursB, contourFoundB = findContour(previousB, frameB, 200, "B")

    if contourFoundA or contourFoundB:
        frameCount += 1

        if frameCount == 3:
            cntsA, boardContoursA = retrieveDartContour(previousA, frameA, 10, "A")
            cntsB, boardContoursB = retrieveDartContour(previousB, frameB, 30, "B")
            hitCount += 1
    
    # cv.imwrite('Images/previousA.jpg', frameA)
    # cv.imwrite('Images/previousB.jpg', frameB)

    key = cv.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv.destroyAllWindows()

stream1.stop()
stream2.stop()