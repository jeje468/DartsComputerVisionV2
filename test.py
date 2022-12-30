import cv2
from difference import *

board = cv.imread('Images/previousB.jpg')
dart = cv.imread('Images/currentB.jpg')

cnts, boardContours, contourFound = retrieveDartContour(board, dart, 20, "B")

maxYCoordinateCenter = max(x['center'][1] for x in contourFound)
contour = []
for i in range(len(contourFound)):
    if contourFound[i]['center'][1] == maxYCoordinateCenter:
        contour = contourFound[i]['cnt']

maxYCoordinate = max(x[0][1] for x in contour)
possibleCoordinates = list(filter(lambda x: x[0][1] == maxYCoordinate, contour))
tipCoordinate = possibleCoordinates[len(possibleCoordinates) // 2]
y = tipCoordinate[0][0]

x_coordinates = []
y_coordinates = []
for i in range(len(contourFound)):
    x_coordinates.append(list(map(lambda x: x[0][0], contourFound[i]['cnt'])))
    y_coordinates.append(list(map(lambda y: y[0][1], contourFound[i]['cnt'])))

y_coordinate = max(y_coordinates)
y_coordinate_idx = y_coordinates.index(y_coordinate, 0, len(y_coordinates))
x_coordinate = x_coordinates[y_coordinate_idx]
    
cv.circle(boardContours, (tipCoordinate[0][0], tipCoordinate[0][1]), 3, (0, 255, 0), -1)

cv.imshow('Contours', boardContours)

cv.waitKey(0)