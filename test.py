import cv2
from difference import *

board = cv.imread('Images/previousB.jpg')
dart = cv.imread('Images/currentB.jpg')

cnts, boardContours, contourFound = retrieveDartContour(board, dart, 10, "B")
