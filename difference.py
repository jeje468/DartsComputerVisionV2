import cv2 as cv
import cvzone as cvz
from contrast import *

def checkDifference(current, previous, fileName):
    diff = current.copy()
    cv.absdiff(current, previous, diff)

    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    (thresh, mask) = cv.threshold(gray, 240, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)

    boardContours, contourFound = cvz.findContours(current, mask, 0)

    cv.imwrite('Images/' + fileName + ".jpg", boardContours)

    return contourFound

def retrieveDartContour(board, dart, area, camera):
    
    # if camera == "A":
    #dart = cv.fastNlMeansDenoisingColored(dart,None,20,20,7,21) 
    #board = cv.fastNlMeansDenoisingColored(board,None,20,20,7,21)
    #cv.imwrite('Images/' + camera + '/grain.jpg', dart)

    # if camera == "B":
    #     board = increaseContrast(board, 20, 150, 0.4)
    #     dart = increaseContrast(dart, 20, 150, 0.4)
    cv.imwrite('Images/' + camera + '/javitott_tabla.jpg', dart)

    diff = board.copy()
    cv.absdiff(board, dart, diff)
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    cv.imwrite('Images/' + camera + '/kulonbseg.jpg', gray)

    res = increaseContrast(gray, 20, 160, 1.5)
    cv.imwrite('Images/' + camera + '/kulonbseg_kontraszt_novelve.jpg', res)

    for i in range(1, 6, 2):
        res = cv.medianBlur(res, i)
    
    cv.imwrite('Images/' + camera + '/median_szures.jpg', res)

    res = increaseContrast(res, 20, 160, 0.4)
    cv.imwrite('Images/' + camera + '/kontraszt_median_utan.jpg', res)

    (thresh, mask) = cv.threshold(res, 240, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
    cv.imwrite('Images/' + camera + '/kuszoboles.jpg', mask)

    cnts = cv.findContours(mask, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)[-2]
    canvas = np.zeros(mask.shape)

    for cnt in cnts:
        if cv.contourArea(cnt) > area:
            cv.drawContours(canvas, [cnt], -1, (255,255,255), thickness=cv.FILLED)
    
    cv.imwrite('Images/' + camera + '/nyil_maszk.jpg', canvas)

    canvas = canvas.astype(np.uint8)
    boardContours, contourFound = cvz.findContours(dart, canvas, 0)

    return cnts, boardContours, contourFound

def findContour(board, dart, area, camera):

    diff = board.copy()
    cv.absdiff(board, dart, diff)
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    cv.imwrite('Images/' + camera + '/difference.jpg', gray)

    for i in range(1, 6, 2):
        gray = cv.medianBlur(gray, i)
    
    cv.imwrite('Images/' + camera + '/mask_before_median.jpg', gray)

    (thresh, mask) = cv.threshold(gray, 50, 255, cv.THRESH_BINARY)

    cv.imwrite('Images/' + camera + '/mask_after_median.jpg', mask)

    cnts = cv.findContours(mask, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)[-2]
    canvas = np.zeros(mask.shape)

    for cnt in cnts:
        if cv.contourArea(cnt) > area:
            cv.drawContours(canvas, [cnt], -1, (255,255,255), thickness=cv.FILLED)
    
    cv.imwrite('Images/' + camera + '/canvas.jpg', canvas)

    canvas = canvas.astype(np.uint8)
    board_contours, contourFound = cvz.findContours(dart, canvas, 0)

    return cnts, board_contours, contourFound

