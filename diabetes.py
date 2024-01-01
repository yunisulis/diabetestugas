import pickle
import streamlit as st


diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))


st.title('Data Mining Prediksi Diabetes')
col1, col2 = st.columns(2)

with col1 :
 Pregnacies = st.text_input ('input nilai Pregnancies')

with col2 : 
 Glucose = st.text_input('input nilai Glucose')

with col1 :
 BloodPress = st.text_input('input nilai BloodPress')

with col2 :
 SkinThickness = st.text_input('input nilai SkinThickness')

with col1 :
 Insulin = st.text_input('input nilai Insulin')

with col2 : 
 BMI = st.text_input('input nilai BMI')

with col1 :
 DiabetesPedigree = st.text_input('input nilai Di')

with col2 :
 Age = st.text_input('input nilai Age')

#code untuk prediksi
diab_diagnosis = ''
if st.button('Test Prediksi Diabtes'):
   diab_prediction = diabetes_model.predict([[Pregnacies, Glucose, BloodPress, SkinThickness, Insulin, BMI, DiabetesPedigree, Age]])

   if(diab_prediction[0] == 1):
     diab_diagnosis = 'Pasien terkena Diabetes'
   else :
    diab_diagnosis = 'Pasien tidak terkena Diabetes'
    
st.success(diab_diagnosis)