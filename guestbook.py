import streamlit as st
import pandas as pd
import requests
from sheet_manager import sheet_manager
from sheet_manager import servsecrets


st.set_page_config(page_title="osu! booth Guestbook",
    page_icon=":heart:", initial_sidebar_state="collapsed")

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

if st.form_submit_button("Submit"):

    # GSheets.sheets_key should be changed to another secret key-value pair
    # To denote another GSheets file for Guest Logbook
    manager = sheet_manager.SheetManager(
        creds = servsecrets.service_acct_creds,
        sheets_key = st.secrets.GSheets.sheets_key
    )

    data_dict = {
        'is_osu_user':[is_osu_user],
        'name':[name],
        'days_attending':[days_attending],
        'message':[message]
    }

    # The sheets must have 4 column names (as per keys in data_dict)
    # that was made before pushing
    manager.push(sheet_number=0, data=pd.DataFrame(data_dict))
    st.success("Guestbook Sign-in Completed!")