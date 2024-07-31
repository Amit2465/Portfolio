import streamlit as st
from PIL import Image
import streamlit_shadcn_ui as ui

# title of this page
st.write('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)
st.title("Amit Yadav")



with st.container():
    left_column, middle_column, right_column = st.columns([1,0.2,0.5] , vertical_alignment="center")
    with left_column:
        st.subheader("Data Analyst")
        st.write('''<p style="text-align: justify;">👋🏻 Hi, I'm Amit! I'm a data science and analytics
                 professional based in Gujarat with a strong background in Data Analysis and Machine 
                 Learning. My experience spans roles in News and Machine Automation sectors. I'm eager 
                 to enhance my data science expertise and pursue broader career goals in this dynamic
                 field.</p>''', unsafe_allow_html=True)
        
        st.write('''<p style="text-align: justify;">👨🏼‍💻 Academic interests: Machine Learning,
                 Data Visualization, Cloud Technology, Software Development</p>''',
                 unsafe_allow_html=True)
        
        st.write('''<p style="text-align: justify;">🏋🏻 In addition, I like to exercise in the gym, run,
                 write, play video games and... enjoy eating good food in my free time!</p>''', 
                 unsafe_allow_html=True)
        
        st.write('''<p style="text-align: justify;">💭 Ideal Career Prospects: Data Analyst, 
                 Data Scientist, Data Engineer </p>''', unsafe_allow_html=True)
        
        st.markdown("</br>", unsafe_allow_html=True)
        ui.link_button(text="Resume", url="#", key="resume_btn")
    
    with middle_column:
        pass
    with right_column:
        Image=Image.open("images/amit_image.png")
        st.image(Image, width=240)