import streamlit as st
st.set_page_config(initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        .st-emotion-cache-1veb5w3{
            background-color:none;
        }
    </style>
    """, unsafe_allow_html=True)


prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
