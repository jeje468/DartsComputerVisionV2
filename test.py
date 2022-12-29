import cv2
from difference import *

dart = cv.imread('Images/currentB.jpg')
board = cv.imread('Images/previousB.jpg')

retrieveDartContour(board, dart, 20, "B")
