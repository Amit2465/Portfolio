import streamlit as st
import json
from streamlit_lottie import st_lottie

@st.cache_data
def load_image(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)
    
    
comingsoon = load_image('images/comingsoon.json')
st_lottie(comingsoon, speed=1, loop=True, width=700, height=400,)     