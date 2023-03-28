import streamlit as st
import os
import requests
import json
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


def retrieve_token(client_id, client_secret, code, redirect_uri):
    """ Retrieves a token derived from the code sent by the osu! API """
    res = requests.post("https://osu.ppy.sh/oauth/token", headers = {
        "Content-Type": "application/json",
        "Accept": "application/x-www-form-urlencoded",
    },
    params={
        "client_id": client_id,
        "client_secret": client_secret,
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": redirect_uri,
    })

    return res.json["token_type"] + " " + res.json()["access_token"]


# This is the client ID for the osu! API
client_id = os.environ.get("CLIENT_ID", 7270)
# This is the redirect URI for the osu! API
redirect_uri = os.environ.get("REDIRECT_URI", "http://127.0.0.1:8501")
# This is the scope for the osu! API
scope = "identity"
# This is the authorization URL for the osu! API
auth_url = create_authorization_url(client_id, redirect_uri, scope)
# This is the authorization code for the osu! API
auth_code = st.experimental_get_query_params().get("code", None)
# This is the access token for the osu! API
access_token = retrieve_token(auth_code)

# We technically don't need this but just in case someone tries to hotlink this page, they have to go through OAuth.
if auth_code and access_token:
    authed_main()
else:
    st.write(f"Please authorize this app to use your osu! account by clicking [here]({auth_url})")
    st.write("You will be redirected to a page where you can authorize this app to access your osu! account.")
    st.write("Once you have authorized this app, you will be redirected back to this page. Please click the button below to continue.")
    st.write("If you are not redirected, please copy and paste the URL from your browser into the address bar of your browser.")
