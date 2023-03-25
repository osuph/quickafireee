import streamlit as st
import intro

view = st.empty()

def app():
    #Get Header
    view.markdown(open("REGISTRATION_HEADER.md").read(), unsafe_allow_html=True)

    with view.form("Registration"):
        username = view.text_input("osu!username", "", 15)
        email = view.text_input("Email", "")
        profile_url = view.text_input("osu!profile URL", "")
        phone_number = view.text_input("Phone Number", "")
        days_attending = view.multiselect("Days Attending", ["Day 1", "Day 2", "Day 3", "All Days"])
        consented_to_dataprivacy = view.checkbox("I consent to the collection of my data for the purposes of this event.")

        submitted = view.form_submit_button("Submit")

        if submitted:
            print("TODO! Submit to Google Sheet!")
            view.empty()
            st.success("Thanks for completing the registration! You will receive an email with further instructions shortly.")
            if st.button("Start over?"):
                intro.app()
