import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Helps Patients Navigate Symptoms", page_icon="🏥")

st.title("The Poliran Hospital🏥-navigateursymptoms😷")

@st.cache_resource
def load_model():
  with open("hospital_model.pkl", "rb" ) as f:
    return pickle.load(f)
    
bundle = load_model()
  
model = bundle['mode']
scaler = bundle['scaler']
features = bundle['features']
cols_to_scale = bundle['cols_to_scale']
gender_map = bundle['gender_map']
temp_map = bundle['temp_map']
hr_map = bundle['hr_map']
dur_map = bundle['dur_map']
cc_map = bundle['cc_map']

st.header("Patient Information")

age = st.number_input("Age", 1, 120, 35)

gender = st.selectbox(
  "Gender",
  ["Female", "Male"]
)

st.header("Symptoms")

fever = st.checkbox("Fever🤒")
cough = st.checkbox("Cough🤧")
headache = st.checkbox("Headache🤕")
chest_pain = st.checkbox("Chest Pain😣🫀")
stomach_pain = st.checkbox("Stomach Pain🤢")
nausea_vomiting = st.checkbox("Nausea/Vomiting🤮")
dizziness = st.checkbox("Dizziness😵‍💫")
skinrash = st.checkbox("Skin Rash🔴🩹")

st.header("Medical Information")

chief_complaint = st.selectbox(
  "Chief Complaint",
  list(cc_map.keys())
)

duration = st.selectbox(
  "Duration",
  list(dur_map.keys())
)

temperature = st.selectbox(
  "Temperature",
  list(temp_map.keys())
)
