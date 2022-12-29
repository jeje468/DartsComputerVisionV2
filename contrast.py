import cv2 as cv
import numpy as np

def increaseContrast(img, lower, upper, gamma):

    img[img > upper] = upper
    img[img < lower] = lower

    img = cv.normalize(img, None, 0, 255, norm_type=cv.NORM_MINMAX, dtype=cv.CV_8UC1)

    lookUpTable = np.empty((1,256), np.uint8)
    for i in range(256):
        lookUpTable[0,i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)

    img = cv.LUT(img, lookUpTable)

    return img