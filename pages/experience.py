import streamlit as st
from streamlit_chat import message

st.set_page_config(initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        .st-emotion-cache-1veb5w3{
            background-color:white;
        }
        .avatar{
            display:none !important;
        }
    </style>
    """, unsafe_allow_html=True)


message("RT @ABCWorldNews: MORE: Three people shot, suspect in custody in Los Angeles airport shooting!", is_user=True)  # align's the message to the right

prompt = st.chat_input("Say something")
# if prompt:
#     st.write(f"User has sent the following prompt: {prompt}")
