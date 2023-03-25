import streamlit as st
import registration

# By default we think they haven't passed yet
passed_evaluation = False
view = st.empty()


def app():
    view.markdown(open("EVALUATION.md").read(), unsafe_allow_html=True)

    # Provide quiz logic here
    if passed_evaluation:
        if st.button("Continue"):
            view.empty()
            registration.app()

