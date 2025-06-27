import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load saved models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# ---------------------- Diabetes Prediction ----------------------
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0)
    with col2:
        Glucose = st.number_input('Glucose Level', min_value=0.0)
    with col3:
        BloodPressure = st.number_input('Blood Pressure value', min_value=0.0)
    with col1:
        SkinThickness = st.number_input('Skin Thickness value', min_value=0.0)
    with col2:
        Insulin = st.number_input('Insulin Level', min_value=0.0)
    with col3:
        BMI = st.number_input('BMI value', min_value=0.0)
    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value', min_value=0.0)
    with col2:
        Age = st.number_input('Age of the Person', min_value=1)

    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        input_data = [
            Pregnancies, Glucose, BloodPressure, SkinThickness,
            Insulin, BMI, DiabetesPedigreeFunction, Age
        ]
        diab_prediction = diabetes_model.predict([input_data])

        diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'

    st.success(diab_diagnosis)

# ---------------------- Heart Disease Prediction ----------------------
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('Age', min_value=1)
    with col2:
        sex = st.number_input('Sex (0 = Female, 1 = Male)', min_value=0, max_value=1, step=1)
    with col3:
        cp = st.number_input('Chest Pain types (0–3)', min_value=0, max_value=3, step=1)
    with col1:
        trestbps = st.number_input('Resting Blood Pressure', min_value=0.0)
    with col2:
        chol = st.number_input('Serum Cholesterol (mg/dl)', min_value=0.0)
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl (0 or 1)', min_value=0, max_value=1, step=1)
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results (0–2)', min_value=0, max_value=2, step=1)
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved', min_value=0.0)
    with col3:
        exang = st.number_input('Exercise Induced Angina (0 or 1)', min_value=0, max_value=1, step=1)
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise', min_value=0.0)
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment (0–2)', min_value=0, max_value=2, step=1)
    with col3:
        ca = st.number_input('Major vessels colored by fluoroscopy (0–3)', min_value=0, max_value=3, step=1)
    with col1:
        thal = st.number_input('Thal (0 = normal; 1 = fixed defect; 2 = reversible defect)', min_value=0, max_value=2, step=1)

    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        input_data = [
            age, sex, cp, trestbps, chol, fbs, restecg,
            thalach, exang, oldpeak, slope, ca, thal
        ]
        heart_prediction = heart_disease_model.predict([input_data])

        heart_diagnosis = 'The person is having heart disease' if heart_prediction[0] == 1 else 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# ---------------------- Parkinson's Prediction ----------------------
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.number_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.number_input('MDVP:Flo(Hz)')
    with col4:
        Jitter_percent = st.number_input('MDVP:Jitter(%)')
    with col5:
        Jitter_Abs = st.number_input('MDVP:Jitter(Abs)')
    with col1:
        RAP = st.number_input('MDVP:RAP')
    with col2:
        PPQ = st.number_input('MDVP:PPQ')
    with col3:
        DDP = st.number_input('Jitter:DDP')
    with col4:
        Shimmer = st.number_input('MDVP:Shimmer')
    with col5:
        Shimmer_dB = st.number_input('MDVP:Shimmer(dB)')
    with col1:
        APQ3 = st.number_input('Shimmer:APQ3')
    with col2:
        APQ5 = st.number_input('Shimmer:APQ5')
    with col3:
        APQ = st.number_input('MDVP:APQ')
    with col4:
        DDA = st.number_input('Shimmer:DDA')
    with col5:
        NHR = st.number_input('NHR')
    with col1:
        HNR = st.number_input('HNR')
    with col2:
        RPDE = st.number_input('RPDE')
    with col3:
        DFA = st.number_input('DFA')
    with col4:
        spread1 = st.number_input('spread1')
    with col5:
        spread2 = st.number_input('spread2')
    with col1:
        D2 = st.number_input('D2')
    with col2:
        PPE = st.number_input('PPE')

    parkinsons_diagnosis = ''

    if st.button("Parkinson's Test Result"):
        input_data = [
            fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP,
            Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR,
            RPDE, DFA, spread1, spread2, D2, PPE
        ]
        parkinsons_prediction = parkinsons_model.predict([input_data])

        parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
