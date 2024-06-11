import streamlit as st

st.title("Hello, Rakshit there")
from streamlit_navigation_bar import st_navbar
page = st_navbar(["Home", "Documentation", "Examples", "Community", "About"])
