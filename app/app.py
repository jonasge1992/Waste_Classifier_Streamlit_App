import streamlit as st
import numpy as np
import requests
from PIL import Image
import io
import os

def send_image_to_api(image):
    # Convert the image to bytes
    img_bytes = io.BytesIO()
    image.save(img_bytes, format='PNG')
    img_bytes = img_bytes.getvalue()

    # Set up the request payload
    files = {'file': ('image.png', img_bytes, 'image/png')}

    # Make the request to the API
    response = requests.post('http://3.144.104.123/predict', files=files)

    return response.json()

# Set page title and background color
st.set_page_config(page_title='Waste Identification App', layout='wide', initial_sidebar_state='collapsed')

# Define app layout and content
st.title('Waste Identification App')
st.write('Welcome to my app. Upload a picture of an item you want to be identified for waste.')

picture = st.camera_input("Take a picture of an item you want to be identified for waste.")


if picture is not None:
    # Display the image
    image = Image.open(picture)
    st.image(image, caption='Captured Image', use_column_width=True)

    # Send the image to the API and get the prediction
    result = send_image_to_api(image)

    # Display the prediction result
    st.write("Prediction:", result["class_name"])

# Custom CSS for styling
st.markdown(
    """
    <style>
        body {
            background-color: #1e1e1e; /* Dark grey background */
            color: #ffffff; /* White text */
        }
        .reportview-container {
            background-color: transparent; /* Ensure transparency for the background color to show */
            flex-direction: row;
        }
        .css-1aumxhk {
            padding: 10px;
            border-radius: 5px;
            box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.1); /* White shadow for dark theme */
            background-color: rgba(30, 30, 30, 0.8); /* Semi-transparent dark grey for readability */
        }
    </style>
    """,
    unsafe_allow_html=True
)
