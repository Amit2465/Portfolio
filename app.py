import streamlit as st



# Set page title
st.set_page_config(
    page_title="Portfolio",
    layout="wide",
    page_icon="desktop_computer",
    initial_sidebar_state="auto"
) 



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
    