import streamlit as st
from streamlit_webrtc import webrtc_streamer

st.set_page_config(
    page_title="push up counter",
    page_icon=":shark:",
    initial_sidebar_state="collapsed",
    layout="wide",
    menu_items={
        'Get Help': 'https://wa.me/6285536956301',
        'Report a bug': "https://wa.me/6285536956301"
    }
)

stream = webrtc_streamer(key = "coba",
                         rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
                         }
                         )