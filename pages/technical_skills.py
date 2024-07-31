import streamlit as st
import streamlit_shadcn_ui as ui

# set page title
st.header("Technical Skills")
st.markdown("</br>", unsafe_allow_html=True)



# Programming languages
col1 , col2 = st.columns((2))
with col1:
    st.markdown("Programming Languages")
with col2:
    ui.badges(badge_list=[("Python", "default"), ("SQL", "default"), ("Java", "default")], class_name="flex gap-2", key="programming_languages")    



# Data Visualization
col3, col4 = st.columns((2))
with col3:
    st.markdown("Data Visualization")
with col4:
    ui.badges(badge_list=[("Matplotlib", "default"), ("Seaborn", "default"), ("Plotly", "default"), ("Power BI", "default")], class_name="flex gap-2", key="data_visualization")  


# Databases
col5, col6 = st.columns((2)) 
with col5:
    st.markdown("Databases and Cloud System")
with col6:
    ui.badges(badge_list=[("MySQL", "default"), ("AWS", "default")], class_name="flex gap-2", key="databases")      
    

# Version Control
col7, col8 = st.columns((2))
with col7:
    st.markdown("Version Control")
with col8:
    ui.badges(badge_list=[("Git", "default"), ("Docker", "default")], class_name="flex gap-2", key="version control")


# front end and back end
col9, col10 = st.columns((2))
with col9:
    st.markdown("Frontend and Backend")
with col10:
    ui.badges(badge_list=[("HTML", "default"), ("CSS", "default"), ("Streamlit", "default")], class_name="flex gap-2", key="frontend_backend")        


# Machine Learning
col11, col12 = st.columns((2))
with col11:
    st.markdown("Machine Learning Frameworks")
with col12:
    ui.badges(badge_list=[("Pandas", "default"), ("Numpy", "default"), ("Scikit-learn", "default")], class_name="flex gap-2", key="data_science_techniques")             


#operating system
col13, col14 = st.columns((2))
with col13:
    st.markdown("Operating Systems")
with col14:
    ui.badges(badge_list=[("Windows", "default"), ("Linux", "default")], class_name="flex gap-2", key="operating_systems")    

#miscellaneous
col13, col14, = st.columns((2))
with col13:
    st.markdown("Miscellaneous")
with col14:
    ui.badges(badge_list=[("Jupyter Notebook", "default"), ("Beautiful Soup", "default"), ("Microsoft Excel", "default")], class_name="flex gap-2", key="miscellaneous")        