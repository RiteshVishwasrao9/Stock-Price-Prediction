import streamlit as st
import pickle
import numpy as np

# Load the pre-trained model from pickle file
with open('stock_price_predictor.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit app title
st.title('Stock Price Prediction')

# User input for SMA50 and SMA200
sma50 = st.number_input('Enter SMA50:', min_value=0.0)
sma200 = st.number_input('Enter SMA200:', min_value=0.0)

# Prediction on button click
if st.button('Predict'):
    # Prepare the input for prediction
    features = np.array([[sma50, sma200]])

    # Model prediction
    prediction = model.predict(features)

    # Display the result
    st.write(f'Predicted Stock Price: {prediction[0]:.2f}')
