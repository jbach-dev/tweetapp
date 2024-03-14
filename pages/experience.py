import streamlit as st
from streamlit_chat import message

st.set_page_config(initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        .st-emotion-cache-1veb5w3{
            background-color:white;
        }
    </style>
    """, unsafe_allow_html=True)


message("My message")
message("Hello bot!", is_user=True)  # align's the message to the right

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
