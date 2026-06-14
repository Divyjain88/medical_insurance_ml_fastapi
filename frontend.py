import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(
    page_title="Medical Insurance Predictor",
    page_icon="💰"
)

st.title("💰 Insurance Premium Predictor")

st.write("Enter customer details below")

# Inputs
age = st.number_input(
    "Age",
    min_value=1,
    max_value=119,
    value=30
)

bmi = st.number_input(
    "BMI",
    min_value=10.0,
    max_value=60.0,
    value=25.0
)

sex = st.selectbox(
    "Gender",
    ["male", "female"]
)

smoker = st.selectbox(
    "Smoker",
    ["yes","no"]
)

children = st.number_input(
    "Number of Children",
    min_value=0,
    max_value=10,
    value=0
)

region = st.selectbox(
    "Region",
    [
        "southwest",
        "southeast",
        "northwest",
        "northeast"
    ]
)


if st.button("Predict Premium"):

    input_data = {
        "age": age,
        "bmi": bmi,
        "smoker": smoker,
        "region": region,
        "children": children,
        "sex": sex
    }
    

    try:
        response = requests.post(API_URL, json=input_data)

        if response.status_code == 200:

            result = response.json()

            prediction = result["response"]

            st.success("Prediction Successful ✅")

            st.metric(
                label="Predicted Premium",
                value=f"₹ {prediction['predicted_premium']:,.2f}"
            )

        else:
            st.error(f"Error {response.status_code}")
            st.write("Response Text:", response.text)

    except requests.exceptions.ConnectionError:
        st.error(
            "❌ Could not connect to FastAPI server.\n\n"
            "Run:\n"
            "uvicorn app:app --reload"
        )

    