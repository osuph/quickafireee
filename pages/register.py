import streamlit as st

st.set_page_config(page_title="osu!Quickfire Registration",
    page_icon=":fire:", initial_sidebar_state="collapsed")

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
    st.text_input("osu!username", st.session_state.get("osu_username", ""), 24)
    st.text_input("Email", "", 24)
    st.text_input("osu!profile URL", f"https://osu.ppy.sh/users/{st.session_state.get('osu_user_id', '')}")
    # Since we may have some LAN tournaments, we can just toggle this and restart the application
    # Since we *might* reuse this beyond CONQUEST 2023
    if st.session_state["CONQUEST_MODE"]:
        st.text_input("Proof of Attendance (Must be a Google Drive Link)", "")
        st.multiselect("Days Attending", ["Day 1", "Day 2", "Day 3", "All Days"])
        st.text_input("Phone Number", "")
    st.checkbox(
        "I consent to the collection of my data as per provisions of the Data Privacy Act of 2012.")

    if st.form_submit_button("Submit"):
        # Google forms logic goes here
        st.success("Thank you for registering! A QR code has been provided.")
