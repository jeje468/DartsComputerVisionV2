import streamlit as st
import time
from gameplayAttributes import *
import json
from gameplay import *

if "selectedPlayers" in st.session_state and "startingPoint" in st.session_state:
    if "gameplayAttributes" not in st.session_state:
        calibrationPoints = []

        with open('calibrationPoints.txt') as f:
            lines = f.readlines()
            for line in lines:
                coordinates = line.rstrip('\n').split(",")
                calibrationPoints.append((int(coordinates[0]), int(coordinates[1])))

        gameplayAttributes = GameplayAttributes(calibrationPoints, st.session_state["selectedPlayers"], st.session_state["startingPoint"])

        for i in range(0, len(gameplayAttributes.players)):
            gameplayAttributes.points.append(0)

        st.session_state["gameplayAttributes"] = gameplayAttributes
        sonStr = json.dumps(gameplayAttributes.__dict__)
        print(sonStr)

if "playerIdx" not in st.session_state:
    st.session_state["playerIdx"] = 0

st.title("Darts computer vision")

if "gameplayAttributes" in st.session_state:

    col1, col2 = st.columns(2)

    with col1:
        currentPlayerText = st.header("Current player: ")
    
    with col2:
        currentPointsText = st.header("Points = 0")

    pointsLabel = st.header("")
    
    placeholder = st.empty()
    nextButton = st.button("Next")
    
    if nextButton:
        currentPlayerText.write("## Current player: " + st.session_state["gameplayAttributes"].players[st.session_state["playerIdx"]])
        currentPointsText.write("## Points = " + str(st.session_state["gameplayAttributes"].points[st.session_state["playerIdx"]]))
        pointsLabel.write("")

        points = startGame(st.session_state["gameplayAttributes"].calibrationPoints)

        stringPoints = []
        sumOfPoints = sum(points)
        for point in points:
            stringPoints.append(str(point))
        
        print(" + ".join(stringPoints))

        pointsLabel.write("## " +  " + ".join(stringPoints) + " = " + str(sumOfPoints))

        st.session_state["gameplayAttributes"].points[st.session_state["playerIdx"]] -= sumOfPoints
        currentPointsText.write("## Points = " + str(st.session_state["gameplayAttributes"].points[st.session_state["playerIdx"]]))

        if st.session_state["playerIdx"] == len(st.session_state["gameplayAttributes"].players) - 1:
            st.session_state["playerIdx"] = 0
        else:
            st.session_state["playerIdx"] += 1

