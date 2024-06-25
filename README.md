This is the waste classifier frontend.

You can find the backend API here https://github.com/jonasge1992/Waste_Classifier. In the EDA_Waste_Classifier.ipynb you can see the model that was trained on the https://www.kaggle.com/datasets/alistairking/recyclable-and-household-waste-classification Recyclable and Household Waste Classification Dataset in order to classify 30 different types of materials in the household for waste with an accuracy of ~68%.

The best model was then saved as a model (h5, json and keras in model folder) and deployed into a Dockerfile (mainly based on the fast.py in the project_waste/api folder).

This is then connected with this interface from Streamlit.

The final app can be tested here: https://wasteclassifier.streamlit.app/
