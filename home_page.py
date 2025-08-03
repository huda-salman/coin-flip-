import streamlit as st


st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f8ff;
    }
    .big-font {
        font-size:50px !important;
        color: darkred;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="big-font">Waoah look who is here !</p>', unsafe_allow_html=True)

st.image("./ocean.jpg",caption="life if you win in all games 1st try 🤗")
st.header(" hop on and test your skills\nlet's see how lucky your are :]!")   

name=st.text_input("what would u like to be called ")


if name =="huda" or name=="Huda":
    st.image("./huda.jpg")
elif name=="zainab" or name=="Zainab":
    st.write(" :red[*huh?!!what? you? lawyer!!!\ndam...(⊙_⊙;)*]")
elif name=="tuqa"or name=="Tuqa":
    st.write(" :blue[*barccaaaa yayay*]")
elif name=="ayah" or name=="Ayah":
    st.write(":red[(❤️ ω ❤️) wifey ]")
elif name=="noor"or name=="Noor":
    st.write("pls make a decision,for the love of god  ")
elif name=="mariam" or name=="maryam" or name=="Mariam "or name=="Maryam":
    st.write("you shortie :], just get tall already cmon (￣▽￣)")
elif name=="mahdei" or name=="Mahdei":
    st.write(":blue[you mean nerdy tech guy ?,sure sure] ")
elif name=="tareq" or name =="Tareq" or name=="Bob":
    st.error("Tareq?!")
    st.text("huh? who ? BOB? oh no its tareq! \ndid you play genshin yet?🤨\n ")
elif name=="mays"or name=="Mays":
    st.text(" من  جنت صغيره صار بيه كمل   \niconic barss🤣  ")

elif name=="gora" or name=="Gora":
    st.text("cutie patootie ")
    st.image("./gora.jpg")

elif name=="saki" or name=="Saki"or name=="mahdi" or name=="Mahdi":
    st.image("./cat.jpg", caption="a cat won't save you, touch some grass.")
elif name=="zahraa" or name=="Zahraa":
    st.text("Hello ZoZo!<3")
    st.image("./zozo_pic.jpg", caption="can't forget about him, can we?")

else:   
    st.write(":blue[hi] "+ name+" 👋🏻")
