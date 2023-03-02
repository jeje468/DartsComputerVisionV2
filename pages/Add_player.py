import streamlit as st

if "players" not in st.session_state:
    players = []
    with open('players.txt') as f:
        lines = f.readlines()
        for line in lines:
            players.append(line)

    st.session_state['players'] = players

st.title("Add players")

playerInput = st.text_input("Add a new player")
addButton = st.button("Add")

with st.expander("Select players"):
    playerMultiSelect = st.multiselect("Select players", st.session_state.players)
    savePlayersButton = st.button("Save players")


if addButton:
    if playerInput not in st.session_state.players:
        st.session_state.players.append(playerInput)

if savePlayersButton:
    #TODO - fix player export
    # f = open("players.txt", "w")
    # f.write("\n".join(st.session_state.players))
    if "selectedPlayers" not in st.session_state:
        st.session_state['selectedPlayers'] = playerMultiSelect

