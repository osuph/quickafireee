import streamlit as st

#Get Header
st.markdown(open("REGISTRATION_INTRO.md").read(), unsafe_allow_html=True)


if st.button("Continue"):
    st.session_state.page_select = "evaluation"

