import streamlit as st
from prediction_helper import predict

st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 0rem;
        }
        h1 {
            margin-top: 0px;
            padding-top: 0px;
        }
    </style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="Health Insurance Cost Predictor", layout="wide")

st.title("Health Insurance Cost Predictor")
# st.markdown("---")

categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer'],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure',
        'Diabetes & High blood pressure', 'Thyroid',
        'Heart disease', 'High blood pressure & Heart disease',
        'Diabetes & Thyroid', 'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# ---------- Personal Information ----------
st.subheader("👤 Personal Information")
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input('Age', min_value=18, max_value=100, step=1)
with col2:
    gender = st.selectbox('Gender', categorical_options['Gender'])
with col3:
    marital_status = st.selectbox('Marital Status', categorical_options['Marital Status'])

# ---------- Financial & Employment ----------
st.subheader("💼 Financial & Employment Details")
col4, col5, col6 = st.columns(3)

with col4:
    income_lakhs = st.number_input('Income (Lakhs)', min_value=0, max_value=200, step=1)
with col5:
    employment_status = st.selectbox('Employment Status', categorical_options['Employment Status'])
with col6:
    number_of_dependants = st.number_input('Number of Dependants', min_value=0, max_value=20, step=1)

# ---------- Health Details ----------
st.subheader("🏥 Health Information")
col7, col8, col9 = st.columns(3)

with col7:
    bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'])
with col8:
    smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'])
with col9:
    genetical_risk = st.number_input('Genetical Risk (0-5)', min_value=0, max_value=5, step=1)

# ---------- Additional Details ----------
st.subheader("📍 Additional Information")
col10, col11, col12 = st.columns(3)

with col10:
    region = st.selectbox('Region', categorical_options['Region'])
with col11:
    medical_history = st.selectbox('Medical History', categorical_options['Medical History'])
with col12:
    insurance_plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'])

# ---------- Insurance Plan ----------
# st.subheader("📄 Insurance Selection")
# insurance_plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'])

st.markdown("---")

if st.button("Predict Premium"):
    input_dict = {
        'Age': age,
        'Number of Dependants': number_of_dependants,
        'Income in Lakhs': income_lakhs,
        'Genetical Risk': genetical_risk,
        'Insurance Plan': insurance_plan,
        'Employment Status': employment_status,
        'Gender': gender,
        'Marital Status': marital_status,
        'BMI Category': bmi_category,
        'Smoking Status': smoking_status,
        'Region': region,
        'Medical History': medical_history
    }

    prediction = predict(input_dict)
    print("AAAAAA: ", prediction)
    st.success(f'Predicted Health Insurance Cost: {prediction}')
    # st.success(f'Predicted Health Insurance Cost: ')