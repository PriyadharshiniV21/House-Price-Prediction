import streamlit as st
from PIL import Image

st.set_page_config(
    page_title = "House Price Prediction",
    layout = "wide",
    initial_sidebar_state = "expanded"
)

st.title('House Price Prediction')

st.write('Hello Folks! Welcome to my _House Price Prediction_ website.')
st.write('Here you will find prices for the houses in **Bengaluru, Karnataka**. Use my prediction website '
         'to find the price of your dream house in Bengaluru.')

st.markdown(
    """
    <style>
        button[title^=Exit]+div [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True
)

image = Image.open('house.jpg')
st.image(image)

st.write('_Happy Predicting!_')

st.sidebar.markdown('## Home')
