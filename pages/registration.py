import streamlit as st

#Get Header
st.markdown(open("REGISTRATION_HEADER.md").read(), unsafe_allow_html=True)

#
# TODO: get defaults from OAuth Callback
with st.form("Registration"):
    username = st.text_input("osu!username", "", 15)
    email = st.text_input("Email", "")
    profile_url = st.text_input("osu!profile URL", "")
    phone_number = st.text_input("Phone Number", "")
    days_attending = st.multiselect("Days Attending", ["Day 1", "Day 2", "Day 3", "All Days"])
    consented_to_dataprivacy = st.checkbox("I consent to the collection of my data for the purposes of this event.")

    submit_button = st.form_submit_button("Submit")

    if submit_button:
        print("TODO! Submit to Google Sheet!")

