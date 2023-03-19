import streamlit as st
from calibrate import *
from gameplay import *
from test import *

if "distances" not in st.session_state:
    st.session_state["distances"] = []

if "points" not in st.session_state:
    st.session_state["points"] = []

if "test2Data" not in st.session_state:
    st.session_state["test2Data"] = []


 
st.title("Test 1")

nextButton = st.button("Next")

calibrationPoints = getCalibrationPoints()

with st.form("test1_form", clear_on_submit=True):
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

    with col1:
        st.write("##")
        detectedHit1 = st.text("Detected hit 1")   
        st.write("##")
        detectedHit2 = st.text("Detected hit 2")   
        st.write("##")
        detectedHit3 = st.text("Detected hit 3")   

    with col2:
        actualHit1 = st.text_input("Actual hit 1")   
        actualHit2 = st.text_input("Actual hit 2")   
        actualHit3 = st.text_input("Actual hit 3")   

    with col3:
        st.write("##")
        detectedX1 = st.text("Detected x 1")
        st.write("##")
        detectedX2 = st.text("Detected x 2")  
        st.write("##")
        detectedX3 = st.text("Detected x 3")   

    with col4:
        actualX1 = st.text_input("Actual x 1")
        actualX2 = st.text_input("Actual x 2")  
        actualX3 = st.text_input("Actual x 3")   

    with col5:
        st.write("##")
        detectedY1 = st.text("Detected y 1")
        st.write("##")
        detectedY2 = st.text("Detected y 2")  
        st.write("##")
        detectedY3 = st.text("Detected y 3") 

    with col6:
        actualY1 = st.text_input("Actual y 1")
        actualY2 = st.text_input("Actual y 2")  
        actualY3 = st.text_input("Actual y 3")

    with col7:
        correct1 = st.text_input("Correct 1")
        correct2 = st.text_input("Correct 2")  
        correct3 = st.text_input("Correct 3")
    
    submitButton = st.form_submit_button("Submit")

if submitButton:

    f = open("testData.txt", "a")
    f.write(str(st.session_state["points"][0]) + ", " + actualHit1 + ", " + st.session_state["distances"][0][0] + ", " + actualX1 + ", " + st.session_state["distances"][0][1] + ", " + actualY1 + ", " + str(correct1) + "\n")
    f.write(str(st.session_state["points"][1]) + ", " + actualHit2 + ", " + st.session_state["distances"][1][0] + ", " + actualX2 + ", " + st.session_state["distances"][1][1] + ", " + actualY2 + ", " + str(correct2) + "\n")
    f.write(str(st.session_state["points"][2]) + ", " + actualHit3 + ", " + st.session_state["distances"][2][0] + ", " + actualX3 + ", " + st.session_state["distances"][2][1] + ", " + actualY3 + ", " + str(correct3) + "\n")
    f.close()
    st.session_state["points"] = []
    st.session_state["distances"] = []

if nextButton:
    st.session_state["points"] = startGame(calibrationPoints, 1000)
    detectedHit1.write(str(st.session_state["points"][0]))
    detectedHit2.write(str(st.session_state["points"][1]))
    detectedHit3.write(str(st.session_state["points"][2]))

    with open('distanceData.txt') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            st.session_state["distances"].append((line.strip().split(",")))
            print(st.session_state["distances"])

            if(i == 0):
                detectedX1.write(line.split(",")[0])
                detectedY1.write(line.split(",")[1].strip())
            elif(i == 1):
                detectedX2.write(line.split(",")[0])
                detectedY2.write(line.split(",")[1].strip())      
            else:
                detectedX3.write(line.split(",")[0])
                detectedY3.write(line.split(",")[1].strip())

    f = open("distanceData.txt", "w")
    f.close()

st.title("Test 2")

emptyButton = st.button("Take empty image")
startButton = st.button("Start")

with st.form("test2_form", clear_on_submit=True):
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

    with col1:
        st.write("##")
        detectedHit = st.text("Detected hit")

    with col2:
        actualHit = st.text_input("Actual hit")  

    with col3:
        st.write("##")
        detectedX = st.text("Detected x") 
    
    with col4:
        actualX = st.text_input("Actual x")
    
    with col5:
        st.write("##")
        detectedY = st.text("Detected y")
    
    with col6:
        actualY = st.text_input("Actual y")
    
    with col7:
        #1 -> single inner, 2 -> triple, 3 -> single outer, 4 -> double
        zone = st.text_input("Zone")



    test2Submit = st.form_submit_button("Submit")

if emptyButton:
    takeEmptyImage()


if startButton:
    point = test2()
    print(point)

    detectedHit.write(str(point))

    with open('distanceData.txt') as f:
        line = f.readlines()[-1]
        detectedX.write(line.split(",")[0])
        detectedY.write(line.split(",")[1].strip())

        st.session_state["test2Data"] = [str(point), line.split(",")[0], line.split(",")[1].strip()]

    f = open("distanceData.txt", "w")
    f.close()

if test2Submit:
    f = open("testData2.txt", "a")
    f.write(st.session_state["test2Data"][0] + ", " + actualHit + ", " + st.session_state["test2Data"][1] + ", " + actualX + ", " + st.session_state["test2Data"][2] + ", " + actualY + ", " + str(zone) + "\n")
    f.close()







