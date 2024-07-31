import streamlit as st
from PIL import Image

st.header("Education")
st.markdown("</br>", unsafe_allow_html=True)


# changing the background color of container
st.markdown("""
    <style>
        .st-emotion-cache-4uzi61 {
            background-color: #F0F2F6 !important; /* Important to override existing styles */
        }
    </style>
""", unsafe_allow_html=True)


college = Image.open("images/Laxmi Institute Of Technology.jpeg")
school = Image.open("images/Andrews.jpeg")
school2 = Image.open("images/Andrews2.jpeg")


with st.container(border=True):
    image_col , text_col = st.columns([2, 5], vertical_alignment='top')
    with image_col:        
        st.image(college, width=200)
    with text_col:
        st.markdown("#### Laxmi Institute of Technology, [Website](https://lit.laxmi.edu.in/)")
        st.markdown("<b>BE</b>- Computer Science and Engineering&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <i>Aug 2019 - July 2023</i>", unsafe_allow_html=True)
        st.markdown("<b>CGPA</b> - `8.4`", unsafe_allow_html=True)


with st.container(border=True):
    image_col , text_col = st.columns([2, 5], vertical_alignment='top')
    with image_col:
        st.image(school, width=200)
    with text_col:
        st.markdown("#### St. Andrew's Higher Secondary School")
        st.markdown("<b>12th</b> - Higher Secondary Education&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <i>June 2018 - July 2019</i>", unsafe_allow_html=True)
        st.markdown("<b>Percentage</b> - `60%`", unsafe_allow_html=True)


with st.container(border=True):
    image_col , text_col = st.columns([2, 5], vertical_alignment='top')
    with image_col:
        st.image(school2, width=200)
    with text_col:
        st.markdown("#### St. Andrew's Higher Secondary School")
        st.markdown("<b>10th</b> - Secondary Education&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <i>June 2016 - July 2017</i>", unsafe_allow_html=True)
        st.markdown("<b>Percentage</b> - `63%`", unsafe_allow_html=True)        