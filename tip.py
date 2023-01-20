import cv2 as cv
import math

angles = [
    [[0, 9], 6],
    [[351, 360], 6],
    [[9, 27], 13],
    [[27, 45], 4],
    [[45, 63], 18],
    [[63, 81], 1],
    [[81, 99], 20],
    [[99, 117], 5],
    [[117, 135], 12],
    [[135, 153], 9],
    [[153, 171], 14],
    [[171, 189], 11],
    [[189, 207], 8],
    [[207, 225], 16],
    [[225, 243], 7],
    [[243, 261], 19],
    [[261, 279], 3],
    [[279, 297], 17],
    [[297, 315], 2],
    [[315, 333], 15],
    [[333, 351], 10]
]

def findTip(boardContours, contourFound, camera):
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
    cv.imwrite('Images/Tip/tip' + camera + ".jpg", boardContours)

    #cv.imshow('Contours', boardContours)

    #cv.waitKey(0)

    return (tipCoordinate[0][0], tipCoordinate[0][1])


#def calculatePoint(tipA, tipB):

def calculatePoint(a, b, ratioA, ratioB):

    xDistInCm = a * ratioA
    yDistInCm = b * ratioB 
    dist = math.sqrt(xDistInCm**2 + yDistInCm**2)

    dotProduct = a * 10 + b * 0
    modOfVector1 = math.sqrt(a * a + b * b) * math.sqrt(10 * 10 + 0 * 0) 
    angle = dotProduct/modOfVector1
    angle = math.degrees(math.acos(angle))

    if b < 0:
        angle = 360 - angle

    point = 0

    for ang in angles:
        if ang[0][0] < angle and angle <= ang[0][1]:
            point = ang[1]
            break

    if 17 < dist:
        point = 0 * point
    elif dist <= 0.635:
        point = 50
    elif 0.635 < dist and dist <= 1.6:
        point = 25
    elif 9.9 <= dist and dist <=10.7:
        point = 3 * point
    elif 16.2 <= dist and dist <= 17:
        point = 2 * point

    return point    
