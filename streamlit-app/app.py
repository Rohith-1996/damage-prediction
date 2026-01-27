from model_helper import predict
import streamlit as st


st.title("Vehicle Damage Prediction")

uploaded_file = st.file_uploader('Upload a file', type = ['png', 'jpg', 'jpeg'])

if uploaded_file:
    image_path = 'temp_file.jpg'
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
        st.image(uploaded_file, caption='Uploaded Image', use_container_width=True)
        prediction = predict(image_path)
        st.info(f'Predicted Class: {prediction}')
