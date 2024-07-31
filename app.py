import streamlit as st



# Set page title
st.set_page_config(
    page_title="Portfolio",
    layout="wide",
    page_icon="desktop_computer",
    initial_sidebar_state="auto"
) 

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)




st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)


# set logo
st.logo("logo.png")


# set pages
p1 = st.Page("pages/about_me.py", title="About Me", icon=":material/person:")
p2 = st.Page("pages/site_overview.py", title="Site Overview", icon=":material/language:")
p3 = st.Page("pages/experience.py", title="Experience", icon=":material/badge:")
p4 = st.Page("pages/technical_skills.py", title="Technical Skills", icon=":material/code:")
p5 = st.Page("pages/project.py", title="Projects", icon=":material/developer_board:")
p6 = st.Page("pages/education.py", title="Education", icon=":material/school:")
p7 = st.Page("pages/certificates.py", title="Certificates", icon=":material/verified_user:")
p8 = st.Page("pages/blog.py", title="Blog", icon=":material/notes:")
p9 = st.Page("pages/contact.py", title="Contact", icon=":material/phone:")
pg = st.navigation([p1,p2, p3, p4, p5, p6, p7, p8, p9])
pg.run()


# footer    
st.markdown('</br>', unsafe_allow_html = True)  
st.markdown("""
<style>
    .badge-container {
        display: flex;
        justify-content: center;
    }
    .badge-container a {
        margin: 0 3px;  
    }
</style>
<hr>
<div class="badge-container">
    <a href="https://www.linkedin.com/in/amit-yadav-674a9722b">
        <img src="https://img.shields.io/badge/-LinkedIn-306EA8?style=flat&logo=Linkedin&logoColor=white" alt="LinkedIn">
    </a>
    <a href="https://github.com/Amit2465">
        <img src="https://img.shields.io/badge/-GitHub-2F2F2F?style=flat&logo=github&logoColor=white" alt="GitHub">
    </a>
    <a href="mailto:your.amityadav23461@gmail.com.com">
        <img src="https://img.shields.io/badge/-Email-D14836?style=flat&logo=gmail&logoColor=white" alt="Email">
    </a>
</div>
</br>
<div style="text-align: center;">© 2024 Amit Yadav</div>
""", unsafe_allow_html=True)    