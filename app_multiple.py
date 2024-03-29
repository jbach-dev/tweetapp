import streamlit as st
import pandas as pd
import requests
from streamlit.components.v1 import html



DATA_URL = 'data_streamlit/presentation.csv'

URL_API = st.secrets['URL_API']

st.set_page_config(page_title="911")

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans:ital,wght@0,100..900;1,100..900&display=swap')

        footer {visibility: hidden;}
        button  {
            background-color:#1DA1F2 !important;
            color:#FFFFFF !important;
            border-color: #1DA1F2 !important;
            border-radius:20px  !important;
            padding:10px 20px 10px 20px !important;
            # margin-top:30% !important;
        }
        .stButton{
            display:flex;
            justify-content:center;
        }
        .css-1y4p8pa{
            padding-bottom:0px;
        }

        .ea3mdgi4 .e1f1d6gn0 .e1f1d6gn1 .e1f1d6gn2 .e1f1d6gn4 .stMarkdown .e1nzilvr5 p {
            border:1px solid rgba(49, 51, 63, 0.2);
            border-radius:20px;
            text-align:center;
            padding:18px;
            color:white;
        }
        .ea3mdgi4 .e1f1d6gn0 .e1f1d6gn1 .e1f1d6gn2 .e1f1d6gn4 .stMarkdown .e1nzilvr5 p a{
            color:white;
        }

        .e1f1d6gn3 .e1f1d6gn0 .e1f1d6gn1 .e1f1d6gn2 .e1f1d6gn4 .stMarkdown .e1nzilvr5 p{
            border:1px solid rgba(49, 51, 63, 0.2);
            border-radius:20px;
            text-align:center;
            padding:18px;
            color:#1DA1F2;
        }

         .e1f1d6gn3 .e1f1d6gn0 .e1f1d6gn1 .e1f1d6gn2 .e1f1d6gn4 .stMarkdown .e1nzilvr5 p a{
             color:#1DA1F2;
        }

        .eczjsme10{
            display:none;
        }

        .eczjsme4{
            padding-top: 3rem;
        }

       #disastertweet, #actionabletweet{
            color:#1DA1F2;
            font-family: "Noto Sans", sans-serif;
        }

        .stLinkButton{
            display:flex;
            justify-content: center;
        }
        .stLinkButton a{
            background-color:#1DA1F2 !important;
            color:#FFFFFF !important;
            border-color: #1DA1F2 !important;
            border-radius:20px  !important;
            padding:10px 20px 10px 20px !important;
        }
    </style>
    """, unsafe_allow_html=True)


@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    # data = data.head(5)
    return data[['tweet_text', 'class_label', 'disaster_year', 'place', 'disaster_type', 'disaster', 'actionable']]

data = load_data(200)

if 'display_tweet' not in st.session_state:
    st.session_state.stage = 0 # 0: Initial, 1: Disaster, 2: Actionable
    st.session_state.display_tweet = data['tweet_text'].sample(frac=1)
    st.session_state.new_tweets = []

def mark_disaster():
    for index in range(0, len(st.session_state.display_tweet)):
        response = requests.get(f'{URL_API}/predict_disaster', { 'tweet': st.session_state.display_tweet.iloc[index] })
        prediction = response.json()
        pred = prediction['tweet_disaster']
        print(pred)
        if round(pred, 2) > 0.3:
            col1.write(st.session_state.display_tweet.iloc[index])
            st.session_state.new_tweets.append(st.session_state.display_tweet.iloc[index])
    st.session_state.stage = 1


def mark_actionable():
    for index in range(0, len(st.session_state.new_tweets)):
        response = requests.get(f'{URL_API}/predict_actionable', { 'tweet': st.session_state.new_tweets[index] })
        prediction = response.json()
        pred = prediction['tweet_actionable']
        print(pred)
        if round(pred, 2) > 0.4:
            col2.write(st.session_state.new_tweets[index])
            col2.link_button(url='https://911-tweet.streamlit.app/experience', label='Answer')

    st.session_state.stage = 2

col1, col2 = st.columns([1, 1], gap="small")

with st.sidebar:
    for index in range(0, len(st.session_state.display_tweet)):
        st.sidebar.write(st.session_state.display_tweet.iloc[index])

with col1:
    st.markdown("<h1 class='title' style='text-align: center;'>Disaster<br>Tweet</h1>", unsafe_allow_html=True)
    st.markdown('---')
    if st.session_state.stage == 0:
        st.button('Find if the tweets are disasters', on_click=mark_disaster, key='button_state')


with col2:
    st.markdown("<h1 class='title' style='text-align: center;'>Actionable<br>Tweet</h1>", unsafe_allow_html=True)
    st.markdown('---')
    if st.session_state.stage == 1:
        st.button('Find if the tweets are actionable', on_click=mark_actionable, key='button_state')
    # if st.session_state.stage == 2:

    # st.button('Answer', href=, key='button_state')
