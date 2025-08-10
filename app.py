# app.py
import streamlit as st
import numpy as np
import joblib
import os

st.set_page_config(page_title="Diabetes Prediction", layout="centered")

st.title("🩺 Diabetes Prediction (Random Forest)")
st.markdown("Enter patient details and click **Predict**. If the app can't find the model/scaler files, upload them below.")

# Try loading model and scaler from disk; if not found, allow upload
def load_from_disk_or_upload():
    model = None
    scaler = None

    # load from disk if present
    if os.path.exists("diabetes_rf_model.pkl"):
        try:
            model = joblib.load("diabetes_rf_model.pkl")
        except Exception as e:
            st.warning("Failed to load diabetes_rf_model.pkl from disk: " + str(e))
    if os.path.exists("scaler.pkl"):
        try:
            scaler = joblib.load("scaler.pkl")
        except Exception as e:
            st.warning("Failed to load scaler.pkl from disk: " + str(e))

    # file upload fallback
    st.sidebar.markdown("### Upload model/scaler (optional)")
    uploaded_model = st.sidebar.file_uploader("Upload diabetes_rf_model.pkl", type=['pkl'])
    uploaded_scaler = st.sidebar.file_uploader("Upload scaler.pkl", type=['pkl'])

    if uploaded_model is not None:
        try:
            model = joblib.load(uploaded_model)
            st.sidebar.success("Model loaded from uploaded file.")
        except Exception as e:
            st.sidebar.error("Can't load uploaded model: " + str(e))

    if uploaded_scaler is not None:
        try:
            scaler = joblib.load(uploaded_scaler)
            st.sidebar.success("Scaler loaded from uploaded file.")
        except Exception as e:
            st.sidebar.error("Can't load uploaded scaler: " + str(e))

    return model, scaler

model, scaler = load_from_disk_or_upload()

if model is None or scaler is None:
    st.warning("Model or scaler not available. Upload them via the sidebar or put them in the app folder.")
    st.stop()

st.markdown("#### Input patient features (same order used in training)")

pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=0)
glucose = st.number_input("Glucose", min_value=0, max_value=300, value=120)
blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=200, value=70)
skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
insulin = st.number_input("Insulin", min_value=0, max_value=900, value=79)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=32.0, format="%.1f")
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=5.0, value=0.5, format="%.3f")
age = st.number_input("Age", min_value=0, max_value=120, value=33)

if st.button("Predict"):
    # ensure order matches training: [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DPF, Age]
    arr = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
    arr_scaled = scaler.transform(arr)
    pred = model.predict(arr_scaled)[0]
    prob = model.predict_proba(arr_scaled)[0][1] if hasattr(model, "predict_proba") else None

    if pred == 1:
        st.error(f"⚠️ Predicted: Likely to have diabetes. (probability ≈ {prob:.2f})" if prob is not None else "⚠️ Predicted: Likely to have diabetes.")
    else:
        st.success(f"✅ Predicted: Unlikely to have diabetes. (probability ≈ {prob:.2f})" if prob is not None else "✅ Predicted: Unlikely to have diabetes.")
