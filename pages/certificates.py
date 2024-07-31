import streamlit as st
from PIL import Image

# changing the background color of container
st.markdown("""
    <style>
        .st-emotion-cache-4uzi61 {
            background-color: #F0F2F6 !important; /* Important to override existing styles */
        }
    </style>
""", unsafe_allow_html=True)


st.header("Certificates")
st.markdown("</br>", unsafe_allow_html=True)


AI = Image.open("images/edunet.jpeg")
python = Image.open("images/Python.jpeg")
pandas = Image.open("images/pandas.jpeg")
sql1 = Image.open("images/sql1.jpg")
sql2 = Image.open("images/sql2.jpg")
shel1 = Image.open("images/shell.jpg")

col1, col2, col3, col4, col5, col6 = st.columns((6), vertical_alignment='top')
with col1:
    with st.container(border = True):
        st.image(AI, width=230)
        st.markdown('''
                        <p style="text-align: center;"><b>Artificial Intelligence</b></p>
                        <p style="text-align: center;">Edunet Foundation & SAP</p>
                    ''', unsafe_allow_html=True)


with col2:
    with st.container(border=True):
        st.image(python, width=230)
        st.markdown('''
                        <p style="text-align: center;"><b>Python Programming </b></p>
                        <p style="text-align: center;">Hackerrank</p>
                    ''', unsafe_allow_html=True)
        
        
with col3:
    with st.container(border=True):
        st.image(pandas, width=230)
        st.markdown("</br>", unsafe_allow_html=True)
        st.markdown("</br>", unsafe_allow_html=True)        
        st.markdown('''
                        <p style="text-align: center;"><b>Pandas </b></p>
                        <p style="text-align: center;">Kaggle</p>
                    ''', unsafe_allow_html=True)


with col4:
    with st.container(border=True):
        st.image(sql1, width=230)
        st.markdown("</br>", unsafe_allow_html=True)
        st.markdown("</br>", unsafe_allow_html=True)        
        st.markdown('''
                        <p style="text-align: center;"><b>Introduction to SQL </b></p>
                        <p style="text-align: center;">Datacamp</p>
                    ''', unsafe_allow_html=True)        
        
        