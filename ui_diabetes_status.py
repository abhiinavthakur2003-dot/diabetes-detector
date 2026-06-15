import streamlit as st
import joblib

model=joblib.load('logistic_regression_model.joblib')
scaler=joblib.load('scaling.joblib')
# st.set_page_config(page_title='Are you Diabetic?',page_icon='🩸💉')
st.set_page_config(page_title='Diabetes Detector',page_icon='🩸💉',layout='centered')


st.title('Diabetes Detector')
st.markdown("""
### 🩸 About this App
Enter your health details in the sidebar and instantly find out if you are at risk of Diabetes using a Machine Learning model trained on real clinical data.
""")
st.warning("⚠️ Disclaimer: This app is for educational purposes only. Do not make medical decisions based on this prediction. Always consult a qualified doctor.")
# Inputs

name=st.sidebar.text_input('Enter your name ')
age=st.sidebar.text_input('Enter your age ')  # later i will type cast it to integer
sleep_hours=st.sidebar.selectbox('How many hours do you sleep?',[3,4,5,6,7,8,9,10])
screen_time = st.sidebar.slider('Select screen time (hours/day)', 0.5, 16.8, 0.5)
familyhistory=st.sidebar.selectbox('Do you have family history of diabeties?',['no','yes'])
hypertensionhistory=st.sidebar.selectbox('Do you have history of hypertension?',['no','yes'])
cardiovascularhistory=st.sidebar.selectbox('Do you have history of cardiovascular disease?',['no','yes'])
bmi=st.sidebar.slider('Select body mass index?',15.0,39.2,15.0)
waist_hip_ratio=st.sidebar.slider('Select waist to hip ratio',0.67,1.06,0.67)
systolic_bp=st.sidebar.slider('Select systolic bp',90,179,90)
diastolic_bp=st.sidebar.slider('Select diastolic bp',50,110,50)
heart_rate=st.sidebar.slider('Select heart rate',40,105,40)
cholesterol_total=st.sidebar.slider('Select cholesterol_total',100,318,100)
hdl_cholesterol=st.sidebar.slider('Select HDL (high-density lipoprotein) cholesterol',20,98,20)
ldl_cholesterol=st.sidebar.slider('Select Low-density lipoprotein (LDL)  cholesterol',50,263,50)
triglycerides=st.sidebar.slider('Select triglycerides levels',30,344,30)
glucose_fasting=st.sidebar.slider('Select glucose_fasting levels',60,172,60)
glucose_postprandial=st.sidebar.slider('Select glucose_postprandial levels',70,287,70)
insulin_level=st.sidebar.slider('Select insulin level',2.0,32.22,2.0)
hbA1c=st.sidebar.slider('Select HbA1c (Hemoglobin A1c)',4.0,9.8,4.0)
gender=st.sidebar.radio('Select Gender',['female','male','other'])
smoking_status=st.sidebar.radio('Do you smoke currently?',['current','former','never'])

# current 
fm_history=0 if familyhistory=='no' else 1
htension_history=0 if hypertensionhistory=='no' else 1
cv_history=0 if cardiovascularhistory=='no' else 1
fg=1 if gender=='female' else 0
mg=1 if gender=='male' else 0
og=1 if gender=='other' else 0
cs_smoker=1 if smoking_status=='current' else 0
fs_smoker=1 if smoking_status=='former' else 0
ns_smoker=1 if smoking_status=='never' else 0



st.subheader('Model Prediction')
try:
    button=st.button('Show Result')
    if button:
        input=([[int(age),sleep_hours,screen_time,fm_history,htension_history,cv_history,bmi,waist_hip_ratio,systolic_bp,diastolic_bp,heart_rate,cholesterol_total,hdl_cholesterol,ldl_cholesterol,triglycerides,glucose_fasting,glucose_postprandial,insulin_level,hbA1c,fg,mg,og,cs_smoker,fs_smoker,ns_smoker]])
        scaled_features=scaler.transform(input)
        prediction=model.predict(scaled_features)
        if prediction[0]==0:
            st.success(f'Good news {name}! Diabetes not diagnosed 😃')
        else:
            st.error(f'{name}, Diabetes diagnosed ⚠️ Please consult a doctor.')

except:
    st.warning('Please fullfill all the details⚠️')

st.markdown("---")
st.caption(
    "Built with ❤️ using Streamlit and Scikit-learn"
)