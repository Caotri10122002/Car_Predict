# Import libraries
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
# Load your dataset
df = pd.read_csv("Car_Purchasing_Data.csv",encoding='latin1')

# App title
st.title("Car Purchase Data Analysis")

# Display the dataset
st.subheader("Dataset Overview")
st.write(df.head())

# Plot 1: Distribution of Car Purchase Amount
st.subheader("Car Purchase Amount Distribution")
fig1, ax1 = plt.subplots()
sns.histplot(df['Car Purchase Amount'], kde=True, ax=ax1, color="blue")
ax1.set_title("Distribution of Car Purchase Amount")
st.pyplot(fig1)

# Plot 2: Scatter Plot of Net Worth vs. Car Purchase Amount
st.subheader("Net Worth vs. Car Purchase Amount")
fig2, ax2 = plt.subplots()
sns.scatterplot(data=df, x="Net Worth", y="Car Purchase Amount", hue="Gender", ax=ax2)
ax2.set_title("Net Worth vs. Car Purchase Amount")
st.pyplot(fig2)

# Plot 3: Annual Salary vs. Car Purchase Amount
st.subheader("Annual Salary vs. Car Purchase Amount")
fig3, ax3 = plt.subplots()
sns.scatterplot(data=df, x="Annual Salary", y="Car Purchase Amount", hue="Gender", ax=ax3)
ax3.set_title("Annual Salary vs. Car Purchase Amount")
st.pyplot(fig3)

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
    """)
