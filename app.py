
import streamlit as st
import joblib

# Load the trained model
model = joblib.load('car_purchase_model.pkl')

st.title("Car Purchase Prediction App")

# Input fields for user to input data
age = st.number_input("Age", min_value=18, max_value=100, step=1)
annual_salary = st.number_input("Annual Salary", min_value=0.0, step=1000.0)
credit_card_debt = st.number_input("Credit Card Debt", min_value=0.0, step=100.0)
net_worth = st.number_input("Net Worth", min_value=0.0, step=1000.0)

# Button to make predictions
if st.button("Predict"):
    prediction = model.predict([[age, annual_salary, credit_card_debt, net_worth]])
    st.write(f"Estimated Car Purchase Amount: ${prediction[0]:.2f}")
    