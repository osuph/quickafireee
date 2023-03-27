import streamlit as st
import os
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="osu!Quickfire Registration",
    page_icon=":fire:", initial_sidebar_state="collapsed")

# HACK: This is to get rid of the sidebar
no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)

# PAGE SETUP ENDS HERE

def create_authorization_url(client_id, redirect_uri, scope):
    """ Returns the authorization URL for the osu! API"""
    return f"https://osu.ppy.sh/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope={scope}"


def authed_main():
    """ The main page for the app,  requires user to be authed firsthand """
    with open("REGISTRATION_INTRO.md", encoding="utf-8") as f:
        st.markdown(f.read(), unsafe_allow_html=True)

    if st.button("Continue"):
        switch_page("evaluation") # type:ignore

if __name__ == "__main__":
    # This is the client ID for the osu! API
    client_id = 7270 or int(os.environ.get("CLIENT_ID"))
    # This is the redirect URI for the osu! API
    redirect_uri = "http://127.0.0.1:8501" or os.environ.get("REDIRECT_URI")
    # This is the scope for the osu! API
    scope = "public+identify"
    # This is the authorization URL for the osu! API
    auth_url = create_authorization_url(client_id, redirect_uri, scope)
    # This is the authorization code for the osu! API
    auth_code = st.experimental_get_query_params().get("code", None)

    if auth_code:
        authed_main()
    else:
        st.write(f"Please authorize this app to use your osu! account by clicking [here]({auth_url})")
        st.write("You will be redirected to a page where you can authorize this app to access your osu! account.")
        st.write("Once you have authorized this app, you will be redirected back to this page. Please click the button below to continue.")
        st.write("If you are not redirected, please copy and paste the URL from your browser into the address bar of your browser.")
