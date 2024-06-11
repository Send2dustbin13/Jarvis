import streamlit as st
from streamlit_navigation_bar import st_navbar

st.title("Hello, Rakshit there")
page = st_navbar(["Home", "Documentation", "Examples", "Community", "About"])
