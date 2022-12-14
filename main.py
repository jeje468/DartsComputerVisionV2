import streamlit as st
import cv2

st.set_page_config(page_title="Main Menu")

st.title("Computer vision darts game")

vid = cv2.VideoCapture(0)
FRAME_WINDOW = st.image([])

while(True):
      
    ret, frame = vid.read()
    
    FRAME_WINDOW.image(frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
vid.release()