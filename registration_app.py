import streamlit as st

st.set_page_config(page_title="osu!Quickfire Registration", page_icon=":fire:")

# These three containers declare both the page's description, the interactible navigation button
# and finally the form(s).
cdesc = st.empty()
intr_btn = st.empty()
frm = st.empty()
current_page = st.session_state.get("current_page", "intro")

def intro():
    import streamlit as st

    with cdesc.container():
        st.markdown(open("REGISTRATION_INTRO.md", encoding="utf-8").read(), unsafe_allow_html=True)

    with intr_btn.container():
        if intr_btn.button("Continue"):
            st.session_state.update({"current_page": "evaluation"})

# BUG: This never gets called... oh well....
def register():
    import streamlit as st

    with cdesc.container():
        st.markdown(open("REGISTRATION_HEADER.md", encoding="utf-8").read(), unsafe_allow_html=True)

    with frm.container():
        reg_frm = frm.form("Registration")

        # Se fields
        reg_frm.text_input("osu!username", "", 15)
        reg_frm.text_input("Email", "")
        reg_frm.text_input("osu!profile URL", "")
        reg_frm.text_input("Phone Number", "")
        reg_frm.multiselect("Days Attending", ["Day 1", "Day 2", "Day 3", "All Days"])
        reg_frm.checkbox("I consent to the collection of my data for the purposes of this event.")

        if reg_frm.form_submit_button("Submit"):
            # Google forms logic goes here
            # TODO: Generate a QR code for them to scan onsite
            st.success("")

def evaluation():
    import streamlit as st

    passed_eval = False

    with cdesc.container():
        st.markdown(open("EVALUATION.md", encoding="utf-8").read(), unsafe_allow_html=True)

    # Quiz logic goes here


    with intr_btn.container():
        # HACK: This is for debugging purposes. Remove this once you have a working quiz logic
        if st.button("DEBUG_CONTINUE"):
            st.session_state.update({"current_page": "register"})

        if passed_eval:
            st.success("You passed the evaluation! You can now register for the tournament.")
            if st.button("Continue"):
                st.session_state.update({"current_page": "register"})

page_flow = {
    "intro": intro,
    "evaluation": evaluation,
    "register": register
}

page_flow[current_page]()
