import streamlit as st
import evaluation

st.set_page_config(page_title="osu! Quickfire Registration", page_icon=":fire:")
view = st.empty()

#  I hate duplication but this has to be done :(
view.markdown(open("REGISTRATION_INTRO.md").read(), unsafe_allow_html=True)

if view.button("Continue"):
    view.empty()
    evaluation.app()
