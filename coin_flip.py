import streamlit as st
import pandas as pd 
from random import choice
st.image(r"C:\Users\huda.luabi\Pictures\Saved Pictures\coin.jpg")

st.title("welcome here! ")
st.subheader("this is a simple game \n so test out your like and enjoy ")
name=st.text_input("what is the nameof the brave sodlier ?")
def coin_flip():
  player=st.selectbox(options=["heads","tails"],label="pick your choice")
  system=choice(["heads","tails"])
  if player==system:
    st.write("player wins, you",name," are super lucky ")
  else:
      st.write("player",name," did not win")
      st.write("try again next time! :blue[*loser*]")
st.text(coin_flip())

