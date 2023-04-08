import streamlit as st

if "players" not in st.session_state:
    players = []
    with open('players.txt') as f:
        line = f.readline()
        playerStrings = line.split(",")
        for player in playerStrings:
            if player != "":
                players.append(player)

    st.session_state['players'] = players

st.title("Add players")

with st.form("add_player_form", clear_on_submit=True):
    playerInput = st.text_input("First please add any new players.")
    addButton = st.form_submit_button("Add")

if addButton:
    if playerInput == "":
        st.warning("Players name can't be empty.")
    else:
        if playerInput not in st.session_state.players:
            st.session_state.players.append(playerInput)
        else:
            st.warning("Such a player already exists")

with st.form("select_form", clear_on_submit=False):
    playerMultiSelect = st.multiselect("Next select the players who would like to play.", st.session_state.players, key="selectedPlayers")
    pointsSelect = st.selectbox("Select the starting points.", list(range(101, 1101, 100)), key="startingPoint")
    saveButton = st.form_submit_button("Save")

if saveButton:
    if len(playerMultiSelect) == 0:
        st.warning("Please select at least one player")
    else:
        f = open("players.txt", "w")
        f.write(",".join(st.session_state.players))
        f.close()

