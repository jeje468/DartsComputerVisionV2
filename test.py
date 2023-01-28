import cv2
from difference import *
from calibrate import *
from tip import *
from difference import *


currentA = cv.imread('Images/currentA.jpg')
currentB = cv.imread('Images/currentB.jpg')

previousA = cv.imread('Images/previousA.jpg')
previousB = cv.imread('Images/previousB.jpg')

retrieveDartContour(previousB, currentA, 15, "B")
