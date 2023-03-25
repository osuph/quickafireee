import streamlit as st

# By default we think they haven't passed yet
passed_evaluation = False

# Provide quiz logic here

if passed_evaluation:
    if st.button("Continue"):
        st.session_state.page_select = "registration"

