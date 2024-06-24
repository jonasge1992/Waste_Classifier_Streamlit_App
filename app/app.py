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


st.write('Welcome to my app')

picture = st.camera_input("Take a picture of an item you want to be identified for waste.")


if picture is not None:
    # Display the image
    image = Image.open(picture)
    st.image(image, caption='Captured Image', use_column_width=True)

    # Send the image to the API and get the prediction
    result = send_image_to_api(image)

    # Display the prediction result
    st.write("Prediction:", result["class_name"])
