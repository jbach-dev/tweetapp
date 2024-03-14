import streamlit as st
from streamlit_chat import message

st.set_page_config(initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        .avatar{
            display:none !important;
        }
        .st-emotion-cache-1veb5w3{
            background-color:white;
        }
        .msg{
            background-color:white;
        }
    </style>
    """, unsafe_allow_html=True)

USER = "user"
ASSISTANT = "assistant"

prompt: str = st.chat_input("Enter a prompt here")

if prompt:
    st.chat_message(USER).write(prompt)
    st.chat_message(ASSISTANT).write(f"You wrote {prompt}")


st.write("RT @ABCWorldNews: MORE: Three people shot, suspect in custody in Los Angeles airport shooting!")

# prompt = st.chat_input("Say something")
# if prompt:
#     st.write(f"User has sent the following prompt: {prompt}")
