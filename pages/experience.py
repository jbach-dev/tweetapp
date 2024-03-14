import streamlit as st
st.set_page_config(initial_sidebar_state="collapsed")

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
