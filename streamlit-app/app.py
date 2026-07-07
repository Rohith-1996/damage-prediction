import os
import requests
import streamlit as st

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

st.title("Vehicle Damage Prediction")

uploaded_file = st.file_uploader('Upload a file', type=['png', 'jpg', 'jpeg'])

if uploaded_file:
    st.image(uploaded_file, caption='Uploaded Image', use_container_width=True)

    with st.spinner('Getting prediction...'):
        try:
            files = {'file': (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
            response = requests.post(f"{BACKEND_URL}/predict", files=files, timeout=30)
            response.raise_for_status()
            prediction = response.json()['prediction']
            st.info(f'Predicted Class: {prediction}')
        except requests.exceptions.RequestException as e:
            st.error(f"Could not reach the prediction service: {e}")
