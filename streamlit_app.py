import streamlit as st
from st_pages import add_page_title, get_nav_from_toml

# 페이지 설정
st.set_page_config(
    page_title='Predicting Personality Traits from Facial Images',
    page_icon=':seven:',
    layout="wide",
    initial_sidebar_state="expanded"
)

# sidebar 설정
nav = get_nav_from_toml(".streamlit/pages_sections.toml")

pg = st.navigation(nav)

add_page_title(pg)

pg.run()