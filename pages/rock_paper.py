import streamlit as st 
from random import choice

st.title("Rock Paper Scissors")
st.subheader("choose your weapon here")
st.button("play again:)")
def THE_GAME():
	system=choice(["rock","paper","scissors"])
	player=st.radio("pick one",["rock","paper","scissors"])
	if player==system:
		st.write("Draw!, try again later:)")

	elif player=="rock" and system=="scissors":
		st.write("player wins!, you're a legend💪🏻")
		st.balloons()

	elif player=="scissors" and system=="paper":
		st.write("player wins!, you're a legend💪🏻")
		st.balloons()

	elif player=="paper" and system=="rock":
		st.write("player wins!, you're a legend💪🏻")
		st.balloons()

	else:
		st.write("player loses!, womp womp 🙂‍↕️")


st.write(THE_GAME())


