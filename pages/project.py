import streamlit as st
from streamlit_lottie import st_lottie
import json


@st.cache_data
def load_image(filepath : str):
    with open(filepath, 'r') as f:
        return json.load(f)


# changing the background color of container
st.markdown("""
    <style>
        .st-emotion-cache-4uzi61 {
            background-color: #F0F2F6 !important; /* Important to override existing styles */
        }
    </style>
""", unsafe_allow_html=True)



st.header("Projects")
st.markdown("</br>", unsafe_allow_html=True)


with st.container(border=True):
    col1 , col2 = st.columns([2, 5], vertical_alignment='top')
    with col1:
        autoeda = load_image('images/Autoeda.json')
        st_lottie(autoeda, speed=1, loop=True, width=200, height=200,)  
    with col2:
        st.markdown("### Autoeda")
        st.markdown('''- <p style = "text-align: justify; ">Independently developed an automated 
                    Exploratory Data Analysis (EDA) web application using Streamlit. Integrated Python 
                    libraries such as Matplotlib and Seaborn for visualizations, and implemented 
                    interactive widgets to facilitate user-driven data exploration.</p>'''
                    , unsafe_allow_html=True)
        st.markdown('''- <p style = "text-align: justify; ">Enhanced data understanding and
                    decision-making capabilities by automating the generation of comprehensive
                    visualizations and statistical summaries. Simplified complex data analysis tasks,
                    empowering users to derive actionable insights efficiently.</p>'''
                    , unsafe_allow_html=True)



with st.container(border=True):
    col1 , col2 = st.columns([2, 5], vertical_alignment='top')
    with col1:
        autoeda = load_image('images/Moneyview.json')
        st_lottie(autoeda, speed=1, loop=True, width=200, height=200,)  
    with col2:
        st.markdown("### Money View")



with st.container(border=True):
    col1 , col2 = st.columns([2, 5], vertical_alignment='top')
    with col1:
        dashboard = load_image("images/Dashboard.json")
        st_lottie(dashboard, speed=1, loop=True, width=200, height=200,)
    with col2:
        st.markdown("### Dashboard")


with st.container(border=True):
    col1 , col2 = st.columns([2, 5], vertical_alignment='top')
    with col1:
        autoeda = load_image('images/chatbot.json')
        st_lottie(autoeda, speed=1, loop=True, width=200, height=200,)  
    with col2:
        st.markdown("### Assist AI")
        

with st.container(border=True):
    col1 , col2 = st.columns([2, 5], vertical_alignment='top')
    with col1:
        autoeda = load_image('images/fraud.json')
        st_lottie(autoeda, speed=1, loop=True, width=200, height=200,)  
    with col2:
        st.markdown("### Online Fraud Detection")
        st.write("- <p style = 'tesxt-align: justify;'>Developed a system independently using the Random Forest method to detect fraud in online transaction</p>", unsafe_allow_html=True)
        st.write("- <p style = 'text-align: justify;' >Implemented a fraud detection model that operates as an intelligent system to identify fraudulent or dishonest activities in online transactions, with an accuracy rate of 83%.</p>", unsafe_allow_html=True)

with st.container(border=True):
    col1 , col2 = st.columns([2, 5], vertical_alignment='top')
    with col1:
        autoeda = load_image('images/customer_churn.json')
        st_lottie(autoeda, speed=1, loop=True, width=200, height=200,)  
    with col2:
        st.markdown("### Customer churn prediction")
        st.write("- <p style = 'text-align: justify;'>Collected and processed diverse customer data, including transaction history, website interactions, and demographics.</p>", unsafe_allow_html=True)
        st.write("- <p style = 'text-align: justify;'>Conducted comprehensive exploratory data analysis and feature selection to optimize model accuracy. Successfully trained, deployed, and refined the churn prediction model for optimal performance in the dynamic e-commerce landscape.</p>", unsafe_allow_html=True)


with st.container(border=True):
    col1 , col2 = st.columns([2, 5], vertical_alignment='top')
    with col1:
        autoeda = load_image('images/loan.json')
        st_lottie(autoeda, speed=1, loop=True, width=200, height=200,)  
    with col2:
        st.markdown("### Loan approval prediction")
        st.markdown('''- <p style = "text-align: justify;">Developed a loan approval prediction model
                    using a Support Vector Machine (SVM) with an accuracy of 83%. The model was built 
                    with Python, leveraging libraries like Pandas, Scikit-learn, and Matplotlib to
                    analyze features such as credit history, income, and loan amount.</p>'''
                    , unsafe_allow_html=True)
        
        st.markdown('''- <p style = "text-align: justify;">Optimized for real-time predictions, the SVM
                    model supports decision-making processes in financial institutions by providing 
                    reliable and actionable insights into loan approval outcomes.</p>''', unsafe_allow_html=True)
        
        
with st.container(border=True):
    col1 , col2 = st.columns([2, 5], vertical_alignment='top')
    with col1:
        autoeda = load_image('images/netflix.json')
        st_lottie(autoeda, speed=1, loop=True, width=200, height=200,)  
    with col2:
        st.markdown("### Netflix EDA")
        st.markdown('''- <p style = "text-align: justify;">Enhanced data understanding and decision-making
                    capabilities by automating the generation of comprehensive visualizations and statistical
                    summaries. Simplified complex data analysis tasks, empowering users to derive actionable 
                    insights efficiently.</p>''', unsafe_allow_html=True)
        st.markdown('''- <p style = "text-align: justify;">Enhanced understanding of Netflix's content 
                    strategy and audience preferences through visualizations and statistical analysis. 
                    Facilitated data-driven decision-making for content acquisition and regional
                    targeting strategies.</p>''', unsafe_allow_html=True)
        