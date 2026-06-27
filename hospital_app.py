import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Helps Patients Navigate Symptoms", page_icon="🏥")

st.title("The Poliran Hospital🏥-🩺navigateursymptoms😷")

@st.cache_resource
def load_model():
  with open("hospital_model.pkl", "rb" ) as f:
    return pickle.load(f)
    
bundle = load_model()
  
model = bundle['model']
scaler = bundle['scaler']
features = bundle['features']
cols_to_scale = bundle['cols_to_scale']
dept_map_inv = bundle['dept_map_inv']
gender_map = bundle['gender_map']
temp_map = bundle['temp_map']
hr_map = bundle['hr_map']
dur_map = bundle['dur_map']
cc_map = bundle['cc_map']

st.header("Patient Information♂️♀️")

age = st.number_input("Age🎂", 1, 120, 35)

gender = st.selectbox(
  "Gender",
  ["Female👩👧♀️", "Male👨👦♂️"]
)

st.header("Symptoms🤒🩺")

fever = st.checkbox("Fever🤒")
cough = st.checkbox("Cough🤧")
headache = st.checkbox("Headache🤕")
chest_pain = st.checkbox("Chest Pain😣🫀")
stomach_pain = st.checkbox("Stomach Pain🤢")
shortness_breath = st.checkbox("Shortness of breath😮‍💨😣")
nausea_vomiting = st.checkbox("Nausea/Vomiting🤮")
dizziness = st.checkbox("Dizziness😵‍💫")
skin_rash = st.checkbox("Skin Rash🔴🩹")

st.header("Medical Information🩺")

chief_complaint = st.selectbox(
  "Chief Complaint📋🩺💬",
  list(cc_map.keys())
)

duration = st.selectbox(
  "Duration📅",
  list(dur_map.keys())
)

temperature_level = st.selectbox(
  "Temperature🌡️",
  list(temp_map.keys())
)

heart_rate_level = st.selectbox(
  "Heart Rate🫀",
  list(hr_map.keys())
)

hypertension = st.checkbox("High Blood Pressure📈🩸")
heart_disease = st.checkbox("Heart Disease🩺🫀")
asthma = st.checkbox("Asthma🫁")

if st.button("Predict Department"):
    patient = pd.DataFrame([{
        'age': age,
        'gender': gender_map.get(gender, 0),
        'fever': int(fever),
        'cough': int(cough),
        'headache': int(headache),
        'chest_pain': int(chest_pain),
        'stomach_pain': int(stomach_pain),
        'shortness_breath': int(shortness_breath),
        'nausea_vomiting': int(nausea_vomiting),
        'dizziness': int(dizziness),
        'skin_rash': int(skin_rash),
        'temperature_level': temp_map.get(temperature_level, 1),
        'heart_rate_level': hr_map.get(heart_rate_level, 1),
        'duration': dur_map.get(duration, 1),
        'asthma': int(asthma),
        'hypertension': int(hypertension),
        'heart_disease': int(heart_disease),
        'chief_complaint': cc_map.get(chief_complaint, 9)
    }])
 
    patient_scaled = patient.copy()
    patient_scaled[cols_to_scale] = scaler.transform(
        patient[cols_to_scale]
    )
 
    prediction = model.predict(
        patient_scaled[features]
    )[0]
 
    department = dept_map_inv[prediction]
 
    st.success(
        f"Recommended Department: {department}"
    )
 
