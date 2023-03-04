import cv2
from difference import *
from calibrate import *
from tip import *
from difference import *

calibrate()
with open('players.txt') as f:
    lines = f.readline()
    players = lines.split(",")
    x = 1
