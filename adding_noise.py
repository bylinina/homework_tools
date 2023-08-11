import streamlit as st
import random
import math
from string import ascii_letters


st.markdown("## A helper tool that introduces noise to text")

noise = st.slider('**Level of noise from 0 to 100:**')
text = st.text_input("**Text you want to add noise to:**", value="Hello world!")

def add_noise(noise, text):
    n_to_swap = math.floor((len(text)*noise)/100)
    sam = random.sample(range(len(text)), n_to_swap)
    text = list(text)
    for ind in sam:
        text[ind] = random.choice(ascii_letters)
    new_text = ''.join(text)
    
    return new_text

#if st.button('Noisify!'):
#    st.write(add_noise(noise, text))

st.write(add_noise(noise, text))