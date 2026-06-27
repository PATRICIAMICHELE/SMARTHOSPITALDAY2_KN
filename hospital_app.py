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
  dur_map = ['dur_map']
  cc_map = ['cc_map']

st.header("Patient Information")

age = st.number_input("Age", 1, 120, 35)

gender = st.selectbox(
  "Gender",
  ["Female", "Male"]
)
