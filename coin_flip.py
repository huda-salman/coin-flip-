import streamlit as st
import pandas as pd 
from random import choice


st.title("welcome here! ")
st.text("this is a simple game \n so test out your like and enjoy ")
def coin_flip():
  player=st.selectbox(options=["heads","tails"],label="pick your choice")
  system=choice(["heads","tails"])
  if player==system:
    st.write("player wins")
  else:
      st.write("player did not win")
st.write(coin_flip())


