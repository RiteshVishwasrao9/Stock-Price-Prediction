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
    # Ensure valid input
    if sma50 and sma200:
        # Prepare the features for prediction
        features = np.array([[sma50, sma200]])

        # Predict the stock price using the loaded model
        prediction = model.predict(features)

        # Flatten the prediction in case it's a multi-dimensional array
        prediction = prediction.flatten()

        # Display the result
        st.write(f'Predicted Stock Price: {prediction[0]:.2f}')
    else:
        st.write('Invalid input data. Please check the inputs for SMA50 and SMA200.')
