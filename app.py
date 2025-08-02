import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model = joblib.load('SVM_model.pkl')
scaler = joblib.load('scaler.pkl')

# Streamlit app title
st.title("Diabetes Prediction App")
st.markdown("Enter the details below to predict whether the person is diabetic.")

# Input fields
pregnancies = st.number_input("Pregnancies", min_value=0, step=1)
glucose = st.number_input("Glucose", min_value=0.0)
blood_pressure = st.number_input("Blood Pressure", min_value=0.0)
skin_thickness = st.number_input("Skin Thickness", min_value=0.0)
insulin = st.number_input("Insulin", min_value=0.0)
bmi = st.number_input("BMI", min_value=0.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0)
age = st.number_input("Age", min_value=0, step=1)

# Predict button
if st.button("Predict"):
    try:
        # Collect input data
        input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness,
                                insulin, bmi, dpf, age]])
        # Scale input
        input_scaled = scaler.transform(input_data)

        # Prediction
        prediction = model.predict(input_scaled)
        result = "Diabetic" if prediction[0] == 1 else "Not Diabetic"
        st.success(f"Prediction: {result}")
    except Exception as e:
        st.error(f"Error during prediction: {e}")

