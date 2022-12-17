import streamlit as st
import cv2 as cv

st.set_page_config(page_title="Main Menu")

st.title("Computer vision darts game")

# run = st.checkbox('Run')
# FRAME_WINDOW_1 = st.image([])
# FRAME_WINDOW_2 = st.image([])
# camera_1 = cv.VideoCapture(0)
# camera_2 = cv.VideoCapture(1)

# while run:
#     _, frame_1 = camera_1.read()
#     _, frame_2 = camera_2.read()

#     frame_1 = cv.cvtColor(frame_1, cv.COLOR_BGR2RGB)
#     frame_2 = cv.cvtColor(frame_2, cv.COLOR_BGR2RGB)

#     FRAME_WINDOW_1.image(frame_1)
#     FRAME_WINDOW_2.image(frame_2)

# else:
#     st.write('Stopped')