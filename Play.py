import streamlit as st
import time
from gameplayAttributes import *
import json

if "selectedPlayers" in st.session_state and "startingPoint" in st.session_state:
    if "gameplayAttributes" not in st.session_state:
        calibrationPoints = []

        with open('calibrationPoints.txt') as f:
            lines = f.readlines()
            for line in lines:
                coordinates = line.rstrip('\n').split(",")
                calibrationPoints.append((coordinates[0], coordinates[1]))

        gameplayAttributes = GameplayAttributes(calibrationPoints, st.session_state["selectedPlayers"], st.session_state["startingPoint"])

        for i in range(0, len(gameplayAttributes.players)):
            gameplayAttributes.points.append(0)

        st.session_state["gameplayAttributes"] = gameplayAttributes
        sonStr = json.dumps(gameplayAttributes.__dict__)
        print(sonStr)

st.title("Darts computer vision")

if "selectedPlayers" in st.session_state:
    text = st.text(str(st.session_state["selectedPlayers"]))
    time.sleep(5)
    text.write("Jani")
