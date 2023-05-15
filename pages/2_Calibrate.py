import streamlit as st
import cv2 as cv
from vidgear.gears import VideoGear
from calibrate import *


st.title("Calibrate cameras")
st.subheader("1. Set the positions of the cameras where the green line intersects with the middle of the board.")

stream1 = VideoGear(source=2, logging=True).start() 
stream2 = VideoGear(source=1, logging=True).start() 

run = st.checkbox('Show webcam feed')
FRAME_WINDOW_A = st.image([])
FRAME_WINDOW_B = st.image([])
camera = cv.VideoCapture(0)

while run:
    frameA = stream1.read()
    frameB = stream2.read()

    cv.line(frameA, (int(frameA.shape[1] / 2), 0), (int(frameA.shape[1] / 2), int(frameA.shape[0])), [0, 255, 0], 3)
    cv.line(frameB, (int(frameB.shape[1] / 2), 0), (int(frameB.shape[1] / 2), int(frameB.shape[0])), [0, 255, 0], 3)

    frameA = cv.cvtColor(frameA, cv.COLOR_BGR2RGB)
    frameB = cv.cvtColor(frameB, cv.COLOR_BGR2RGB)

    cv.imwrite("Images/calibrationLine.jpg", frameB)

    FRAME_WINDOW_A.image(frameA)
    FRAME_WINDOW_B.image(frameB)

stream1.stop()
stream2.stop()


calibrationLabelValues = ["Top camera empty", "Top camera left", "Top camera right", "Side camera empty", "Side camera top", "Side camera bottom", "Done"]
if "calibrationIdx" not in st.session_state:
    st.session_state['calibrationIdx'] = 0
if 'buttonDisabled' not in st.session_state:
    st.session_state['buttonDisabled'] = False


st.subheader("2. Take six calibration photos of the board.")
calibrationText = st.text(calibrationLabelValues[st.session_state['calibrationIdx']])
calibrateButton = st.button("Take a photo", disabled= st.session_state['buttonDisabled'])

if calibrateButton:
    if st.session_state['calibrationIdx'] <= 5:
        takePhoto(st.session_state['calibrationIdx'])
        st.session_state['calibrationIdx'] += 1
        calibrationText.write(calibrationLabelValues[st.session_state['calibrationIdx']])

    if st.session_state['calibrationIdx'] == 6:
        st.session_state['calibrationIdx'] = 0
        st.session_state['buttonDisabled'] = True
        calibrate()



