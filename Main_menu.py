import streamlit as st
import cv2 as cv
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer

st.set_page_config(page_title="Main Menu")

class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")

        img = cv.cvtColor(cv.Canny(img, 100, 200), cv.COLOR_GRAY2BGR)

        return img


st.title("Computer vision darts game")

webrtc_streamer(key="streamer1", video_transformer_factory=VideoTransformer)
webrtc_streamer(key="streamer2")

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