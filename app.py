import streamlit as st
import joblib

# Load the trained model
model = joblib.load("model.pkl")

st.title("Yearly Amount Predictor")

# Input fields for four features
feature1 = st.number_input("Average Session length(in mins)", value=0.0)
feature2 = st.number_input("Time on App(in hrs)", value=0.0)
feature3 = st.number_input("Time on website(in hrs)", value=0.0)
feature4 = st.number_input("Length of Membership(in years)", value=0.0)

if st.button("Predict"):
    x = [[feature1, feature2, feature3, feature4]]
    y_pred = model.predict(x)
    st.success(f"The yearly amount spent by the user is : {y_pred[0]}")