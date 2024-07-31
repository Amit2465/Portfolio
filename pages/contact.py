import streamlit as st
import json
from streamlit_lottie import st_lottie
import streamlit_shadcn_ui as ui


@st.cache_data
def load_image(filepath : str):
    with open(filepath, 'r') as f:
        return json.load(f)
    
  
    
st.header("Contact")
st.markdown("</br>", unsafe_allow_html=True)

col1, col2 = st.columns([2.3, 1], vertical_alignment='top')
with col2:
    contact = load_image('images/Contact.json')
    st_lottie(contact, speed=1, loop=True, width=240, height=240,)
with col1:
    with ui.card(key="card1"):
        ui.element("span", children=["Email"], className="text-gray-400 text-sm font-medium m-1", key="label1")
        ui.element("input", key="email_input", placeholder="Enter your email")

        ui.element("span", children=["Name"], className="text-gray-400 text-sm font-medium m-1", key="label2")
        ui.element("input", key="username_input", placeholder="Enter your name")
        
        ui.element("span", children=["Message"], className="text-gray-400 text-sm font-medium m-1", key="label3")
        ui.element("textarea", key="Message_input", placeholder="Enter your message")
        
        ui.element("button", text="Send", key="button", className="m-1")    