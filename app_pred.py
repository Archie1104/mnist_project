import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image, ImageOps

# Load the pre-trained model
model = tf.keras.models.load_model('mnist_model.h5')

# Streamlit app UI
st.title('MNIST Digit Classifier')
st.write('Upload a 28x28 grayscale image of a handwritten digit (JPG, PNG, or JPEG).')

# File uploader
uploaded_file = st.file_uploader('Choose an image...', type=['jpg', 'png', 'jpeg'])
if uploaded_file is not None:
    # Preprocess the image
    image = Image.open(uploaded_file).convert('L')     # Convert to grayscale
    image = ImageOps.invert(image)  
    image = ImageOps.invert(image)                        # Invert (white background, black digit)
    image = image.resize((28, 28))                      # Resize to 28x28
    img_array = np.array(image) / 255.0                 # Normalize
    img_array = img_array.reshape(1, 28, 28, 1)         # Add batch and channel dimensions

    # Display the image
    st.image(image, caption='Uploaded Image', width=150)

    # Predict
    prediction = model.predict(img_array)
    predicted_digit = np.argmax(prediction)

    # Display the result
    st.write(f'Prediction: **{predicted_digit}**')

