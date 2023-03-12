import streamlit as st
import time
from gameplayAttributes import *
import json
from gameplay import *
from outshot import *

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
            gameplayAttributes.shots.append([])

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
    outshotText = st.header("")
    
    with st.form("add_player_form", clear_on_submit=True):
        col3, col4, col5 = st.columns(3)

        with col3:
            hit1 = st.text_input("First hit")
        
        with col4:
            hit2 = st.text_input("Second hit")
        
        with col5:
            hit3 = st.text_input("Third hit")
        
        changePointsButton = st.form_submit_button("Change points")
    

    nextButton = st.button("Next")

    if changePointsButton:
        pointsSetByPlayer = [hit1, hit2, hit3]
        playerIdx = 0 if len(st.session_state["gameplayAttributes"].players) == 1 else st.session_state["playerIdx"] - 1
        sumOfPoints = sum(st.session_state["gameplayAttributes"].shots[playerIdx][-1])
        currentPoints = st.session_state["gameplayAttributes"].points[playerIdx]
        st.session_state["gameplayAttributes"].points[playerIdx] = currentPoints + sumOfPoints

        for i in range(len(pointsSetByPlayer)):
            if pointsSetByPlayer[i] != "":
                st.session_state["gameplayAttributes"].shots[playerIdx][-1][i] = pointsSetByPlayer[i]
        
        sumOfPoints = sum(map(int, st.session_state["gameplayAttributes"].shots[playerIdx][-1]))
        pointsLabel.write("## " +  " + ".join(map(str, st.session_state["gameplayAttributes"].shots[playerIdx][-1])) + " = " + str(sumOfPoints))

        
        if st.session_state["gameplayAttributes"].points[playerIdx] - sumOfPoints > 0:
            st.session_state["gameplayAttributes"].points[playerIdx] -= sumOfPoints
            currentPlayerText.write("## Current player: " + st.session_state["gameplayAttributes"].players[playerIdx])
            currentPointsText.write("## Points = " + str(st.session_state["gameplayAttributes"].points[playerIdx]))
        
    
    if nextButton:
        currentPlayerText.write("## Current player: " + st.session_state["gameplayAttributes"].players[st.session_state["playerIdx"]])
        currentPointsText.write("## Points = " + str(st.session_state["gameplayAttributes"].points[st.session_state["playerIdx"]]))
        pointsLabel.write("")
        outshotText.write("## Outshot: " + calculateOuthsot(st.session_state["gameplayAttributes"].points[st.session_state["playerIdx"]]))

        points = startGame(st.session_state["gameplayAttributes"].calibrationPoints, st.session_state["gameplayAttributes"].points[st.session_state["playerIdx"]])

        sumOfPoints = sum(points)
    
        pointsLabel.write("## " +  " + ".join(map(str, points)) + " = " + str(sumOfPoints))

        if st.session_state["gameplayAttributes"].points[st.session_state["playerIdx"]] - sumOfPoints > 0:
            st.session_state["gameplayAttributes"].points[st.session_state["playerIdx"]] -= sumOfPoints
            st.session_state["gameplayAttributes"].shots[st.session_state["playerIdx"]].append(points)
            currentPointsText.write("## Points = " + str(st.session_state["gameplayAttributes"].points[st.session_state["playerIdx"]]))

        if st.session_state["playerIdx"] == len(st.session_state["gameplayAttributes"].players) - 1:
            st.session_state["playerIdx"] = 0
        else:
            st.session_state["playerIdx"] += 1

