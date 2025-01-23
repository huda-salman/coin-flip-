import streamlit as st
import pandas as pd 
from random import choice

st.title("welcome here! ")
st.subheader("this is a simple game \n so test out your like and enjoy ")
def coin_flip():
  player=st.radio(options=["heads","tails"],label="pick your choice")
  system=choice(["heads","tails"])
  if player==system:
    st.write("player wins, you are super lucky 🙂‍↕️")
    st.balloons()
  else:
      st.write("player did not win\ntry again next time! :blue[*loser*] 🤡")

st.button("play here !")
st.write(coin_flip())