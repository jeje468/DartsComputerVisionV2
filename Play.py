import streamlit as st
import time

st.title("Darts computer vision")

if "selectedPlayers" in st.session_state:
    text = st.text(str(st.session_state["selectedPlayers"]))
    time.sleep(5)
    text.write("Jani")
