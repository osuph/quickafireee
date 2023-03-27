import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="osu!Quickfire Registration",
    page_icon=":fire:", initial_sidebar_state="collapsed")

# We are coming from an OAuth Callback so we must set our session states

# HACK: This is to get rid of the sidebar
no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)


with open("REGISTRATION_INTRO.md", encoding="utf-8") as f:
    st.markdown(f.read(), unsafe_allow_html=True)

if st.button("Continue"):
    switch_page("evaluation") # type:ignore
