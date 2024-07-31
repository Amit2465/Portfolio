import streamlit as st
from PIL import Image


# set title of the page
st.header("Experience")
st.markdown("</br>", unsafe_allow_html=True)


# import image from local file
analytics_drift = Image.open("images/Analytics drift.jpeg")
machstatz = Image.open("images/Machstatz.Jpeg")
softyoug = Image.open("images/Softyoug.jpeg")


# changing the background color of container
st.markdown("""
    <style>
        .st-emotion-cache-4uzi61 {
            background-color: #F0F2F6 !important; /* Important to override existing styles */
        }
    </style>
""", unsafe_allow_html=True)


# creating a container for all experience
with st.container(border=True):
    image_col , text_col = st.columns([2, 5], vertical_alignment='top')
    with image_col:        
        st.image(analytics_drift, width=200)
    with text_col:
        st.markdown("#### Data Analyst, [Analytics Drift](https://analyticsdrift.com/)")
        st.markdown("<i>Jan 2024 to Present</i>", unsafe_allow_html=True) 
        st.markdown('''<p style = "text-align: justify;">Experienced in Python and Beautiful Soup for
                    web crawling and data collection, proficiently integrating AWS for secure data
                    storage. Skilled in processing large datasets efficiently and conducting insightful
                    data analysis to drive informed decision-making. Proficiently hosts two company
                    websites on AWS Lightsail.</p>''', unsafe_allow_html=True)


with st.container(border=True):
    image_col , text_col = st.columns([2, 5], vertical_alignment='center')
    with image_col:
        st.image(machstatz, width=200)
    with text_col:
        st.markdown("#### Machine Learning Intern, [Machstatz](https://machstatz.com/)")
        st.markdown("<i>Feb 2023 to May 2023</i>", unsafe_allow_html=True)
        st.markdown('''- <p style = "text-align: justify;">Designed and implemented InfluxDB-based Time
                    Series Databases for IOT Sensor data. Proficient in Flux for complex queries, RxPY
                    for reactive programming, and efficient data processing. Collaborated cross-functionally
                    for in-depth data analysis, supporting data-driven decisions aligned with 
                    organizational objectives</p>''', unsafe_allow_html=True)         


with st.container(border=True):
    image_col , text_col = st.columns([2, 5], vertical_alignment='center')
    with image_col:
        st.image(softyoug, width=200)
    with text_col:
        st.markdown("#### Database Developer Intern, [Softyoug](https://softyoug.com/)")
        st.markdown("<i>June 2022 to July 2022</i>", unsafe_allow_html=True)
        st.write('''- <p style = 'text-align: justify;'>Contributed to SQL database development, design,
                 and maintenance, ensuring reliability. Proficient in precise SQL  query writing and
                 execution. Designed and implemented robust database backup and recovery processes,
                 ensuring  data integrity. Collaborated on efficient database management solutions,
                 fostering streamlined operations.  Proactively resolved issues and optimized
                 performance for enhanced efficiency and data accessibility.</p>''', unsafe_allow_html=True )