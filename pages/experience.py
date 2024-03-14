import streamlit as st
from streamlit_chat import message

st.set_page_config(initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        .e1nzilvr5{
            width:70%;
        }
        .st-emotion-cache-1veb5w3{
            background-color:white;
        }

        .stMarkdown{
            display: flex;
            justify-content: right;
        }

        .e1nzilvr5 p{
            text-align:right;
            background-color:#1DA1F2;
            font-family: "Noto Sans", sans-serif;
            padding:10px 20px 10px 20px;
            color:white;
            border-radius:20px;
        }

    </style>
    """, unsafe_allow_html=True)


prompt: str = st.chat_input("Enter a prompt here")

st.write("RT @ABCWorldNews: MORE: Three people shot, suspect in custody in Los Angeles airport shooting!")
