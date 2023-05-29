import streamlit as st
import requests


st.set_page_config(page_title="osu! booth Guestbook",
    page_icon=":heart:")

# HACK: This is to get rid of the sidebar
no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)

# Get header
with open("GUESTBOOK_HEADER.md", "r", encoding="utf-8") as f:
    st.markdown(f.read(), unsafe_allow_html=True)

is_osu_user = st.checkbox("Are you an osu! player?")
name = st.text_input("Your Name (doesn't have to be your real name)")
days_attending = st.selectbox("What Day are you attending?",
                              ["Day 1", "Day 2", "Day 3", "All Days"])
message = st.text_area("Leave a message for us!")
