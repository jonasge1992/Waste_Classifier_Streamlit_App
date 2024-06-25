import streamlit as st
import numpy as np
import requests
from PIL import Image
import io
import os

class_labels_translation = {
    'aerosol_cans': 'Aerosol Cans',
    'aluminum_food_cans': 'Aluminum Food Cans',
    'aluminum_soda_cans': 'Aluminum Soda Cans',
    'cardboard_boxes': 'Cardboard Boxes',
    'cardboard_packaging': 'Cardboard Packaging',
    'clothing': 'Clothing',
    'coffee_grounds': 'Coffee Grounds',
    'disposable_plastic_cutlery': 'Disposable Plastic Cutlery',
    'eggshells': 'Eggshells',
    'food_waste': 'Food Waste',
    'glass_beverage_bottles': 'Glass Beverage Bottles',
    'glass_cosmetic_containers': 'Glass Cosmetic Containers',
    'glass_food_jars': 'Glass Food Jars',
    'magazines': 'Magazines',
    'newspaper': 'Newspaper',
    'office_paper': 'Office Paper',
    'paper_cups': 'Paper Cups',
    'plastic_cup_lids': 'Plastic Cup Lids',
    'plastic_detergent_bottles': 'Plastic Detergent Bottles',
    'plastic_food_containers': 'Plastic Food Containers',
    'plastic_shopping_bags': 'Plastic Shopping Bags',
    'plastic_soda_bottles': 'Plastic Soda Bottles',
    'plastic_straws': 'Plastic Straws',
    'plastic_trash_bags': 'Plastic Trash Bags',
    'plastic_water_bottles': 'Plastic Water Bottles',
    'shoes': 'Shoes',
    'steel_food_cans': 'Steel Food Cans',
    'styrofoam_cups': 'Styrofoam Cups',
    'styrofoam_food_containers': 'Styrofoam Food Containers',
    'tea_bags': 'Tea Bags'
}


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

    proper_name = class_labels_translation[result["class_name"]]

    # Display the prediction result
    st.write("Prediction:", proper_name)

# Custom CSS for styling
st.markdown(
    """
    <style>
        body {
            background-color: #1e1e1e !important; /* Dark grey background */
            color: #ffffff; /* White text */
        }
        .reportview-container {
            background-color: transparent; /* Ensure transparency for the background color to show */
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
