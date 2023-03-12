import cv2
from difference import *
from calibrate import *
from tip import *
from difference import *
from gameplay import *

calibrationPoints = []

with open('calibrationPoints.txt') as f:
    lines = f.readlines()
    for line in lines:
        coordinates = line.rstrip('\n').split(",")
        calibrationPoints.append((int(coordinates[0]), int(coordinates[1])))

startGame(calibrationPoints, 10)
