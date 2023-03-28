# A lightweight version of the main application for debugging purposes. This skips the OAuth step since we need
# To test the core flow of the app.
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="osu!Quickfire Registration (DEBUG)",
    page_icon=":fire:", initial_sidebar_state="collapsed")

with open("REGISTRATION_INTRO.md", encoding="utf-8") as f:
    st.markdown(f.read(), unsafe_allow_html=True)

if st.button("Continue"):
    switch_page("evaluation") #type:ignore
