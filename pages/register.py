import streamlit as st

# HACK: This is to get rid of the sidebar
no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)

with open("REGISTRATION_HEADER.md", encoding="utf-8") as f:
    st.markdown(f.read(), unsafe_allow_html=True)

with st.form("registration_form"):
    # TODO: Autofill this from the OAuth Callback
    st.text_input("osu!username", "", 24)
    st.text_input("Email", "")
    st.text_input("osu!profile URL", "")
    st.text_input("Phone Number", "")
    st.multiselect("Days Attending", ["Day 1", "Day 2", "Day 3", "All Days"])
    st.checkbox("I consent to the collection of my data for the purposes of this event.")

    if st.form_submit_button("Submit"):
        # Google forms logic goes here
        st.success("Thank you for registering! A QR code has been provided.")
