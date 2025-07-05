import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# ---------------- PAGE CONFIG -------------------
st.set_page_config(page_title="Multi Disease Prediction", layout="wide")

# ---------------- LANGUAGE SETUP -------------------
lang = st.selectbox("\U0001F310 Select Language", ["English", "Hindi", "Telugu"], key="lang")

translations = {
    "English": {
        "title": "Multiple Disease Prediction System",
        "diabetes": "Diabetes Prediction",
        "heart": "Heart Disease Prediction",
        "parkinsons": "Parkinson's Prediction",
        "diab_result_btn": "Diabetes Test Result",
        "heart_result_btn": "Heart Disease Test Result",
        "parkinsons_result_btn": "Parkinson's Test Result",
        "diab_yes": "⚠️ The person is diabetic",
        "diab_no": "✅ The person is not diabetic",
        "heart_yes": "⚠️ The person has heart disease",
        "heart_no": "✅ The person does not have heart disease",
        "park_yes": "⚠️ The person has Parkinson's disease",
        "park_no": "✅ The person does not have Parkinson's disease",
        "diab_tips": "\n**Preventive Measures for Diabetes:**\n- Maintain a healthy diet with low sugar intake\n- Exercise regularly\n- Monitor blood glucose levels\n- Maintain a healthy weight\n- Avoid smoking and alcohol\n",
        "heart_tips": "\n**Preventive Measures for Heart Disease:**\n- Eat a balanced diet low in saturated fat and cholesterol\n- Regular physical activity (30 mins/day)\n- Manage stress\n- Avoid smoking\n- Monitor blood pressure and cholesterol levels\n",
        "parkinsons_tips": "\n**Preventive & Lifestyle Tips for Parkinson’s:**\n- Regular exercise (e.g., walking, swimming)\n- Balanced diet rich in fiber and antioxidants\n- Maintain social and mental engagement\n- Follow prescribed medications strictly\n- Consult neurologist regularly\n"
    },
    "Hindi": {
        "title": "मल्टीपल डिजीज प्रेडिक्शन सिस्टम",
        "diabetes": "मधुमेह का पूर्वानुमान",
        "heart": "हृदय रोग का पूर्वानुमान",
        "parkinsons": "पार्किंसन का पूर्वानुमान",
        "diab_result_btn": "मधुमेह परीक्षण परिणाम",
        "heart_result_btn": "हृदय रोग परीक्षण परिणाम",
        "parkinsons_result_btn": "पार्किंसन परीक्षण परिणाम",
        "diab_yes": "⚠️ व्यक्ति मधुमेह से पीड़ित है",
        "diab_no": "✅ व्यक्ति मधुमेह से पीड़ित नहीं है",
        "heart_yes": "⚠️ व्यक्ति को हृदय रोग है",
        "heart_no": "✅ व्यक्ति को हृदय रोग नहीं है",
        "park_yes": "⚠️ व्यक्ति को पार्किंसन रोग है",
        "park_no": "✅ व्यक्ति को पार्किंसन रोग नहीं है",
        "diab_tips": "\n**मधुमेह के लिए रोकथाम के उपाय:**\n- कम चीनी युक्त स्वस्थ आहार लें\n- नियमित रूप से व्यायाम करें\n- रक्त शर्करा स्तर की निगरानी करें\n- स्वस्थ वजन बनाए रखें\n- धूम्रपान और शराब से बचें\n",
        "heart_tips": "\n**हृदय रोग के लिए रोकथाम के उपाय:**\n- संतुलित और कम वसा युक्त आहार लें\n- प्रतिदिन कम से कम 30 मिनट व्यायाम करें\n- तनाव का प्रबंधन करें\n- धूम्रपान से बचें\n- रक्तचाप और कोलेस्ट्रॉल की नियमित जांच करें\n",
        "parkinsons_tips": "\n**पार्किंसन के लिए जीवनशैली सुझाव:**\n- नियमित व्यायाम करें (जैसे चलना, तैराकी)\n- फाइबर और एंटीऑक्सिडेंट युक्त संतुलित आहार लें\n- सामाजिक और मानसिक गतिविधियों में भाग लें\n- दवाओं का नियमित सेवन करें\n- न्यूरोलॉजिस्ट से परामर्श करें\n"
    },
    "Telugu": {
        "title": "బహుళ వ్యాధి అంచనా వ్యవస్థ",
        "diabetes": "డయాబెటిస్ అంచనా",
        "heart": "హృదయ సంబంధిత వ్యాధి అంచనా",
        "parkinsons": "పార్కిన్సన్ అంచనా",
        "diab_result_btn": "డయాబెటిస్ ఫలితం",
        "heart_result_btn": "హార్ట్ డిసీజ్ ఫలితం",
        "parkinsons_result_btn": "పార్కిన్సన్ ఫలితం",
        "diab_yes": "⚠️ వ్యక్తికి డయాబెటిస్ ఉంది",
        "diab_no": "✅ వ్యక్తికి డయాబెటిస్ లేదు",
        "heart_yes": "⚠️ వ్యక్తికి హార్ట్ డిసీజ్ ఉంది",
        "heart_no": "✅ వ్యక్తికి హార్ట్ డిసీజ్ లేదు",
        "park_yes": "⚠️ వ్యక్తికి పార్కిన్సన్ ఉంది",
        "park_no": "✅ వ్యక్తికి పార్కిన్సన్ లేదు",
        "diab_tips": "\n**డయాబెటిస్ నివారణకు చిట్కాలు:**\n- తక్కువ చక్కెర కలిగిన ఆహారం తీసుకోండి\n- నిత్యం వ్యాయామం చేయండి\n- బ్లడ్ షుగర్ స్థాయిలను పరీక్షించండి\n- తగిన బరువును నిర్వహించండి\n- ధూమపానం మరియు మద్యం నివారించండి\n",
        "heart_tips": "\n**హార్ట్ డిసీజ్ నివారణకు చిట్కాలు:**\n- తక్కువ కొవ్వు మరియు కొలెస్ట్రాల్ ఉన్న ఆహారం తీసుకోండి\n- ప్రతి రోజు కనీసం 30 నిమిషాలు వ్యాయామం చేయండి\n- ఒత్తిడిని నియంత్రించండి\n- ధూమపానం నివారించండి\n- బీపీ మరియు కొలెస్ట్రాల్ స్థాయిలను తనిఖీ చేయండి\n",
        "parkinsons_tips": "\n**పార్కిన్సన్ నివారణకు మరియు జీవనశైలి చిట్కాలు:**\n- నడక, ఈత వంటి వ్యాయామాలు చేయండి\n- ఫైబర్ మరియు యాంటీఆక్సిడెంట్లు ఉన్న ఆహారం తీసుకోండి\n- మానసిక, సామాజిక చురుకుతనాన్ని కొనసాగించండి\n- మందులను సమయానికి తీసుకోండి\n- న్యూరాలజిస్టును సంప్రదించండి\n"
    }
}

tr = translations[lang]

# Load saved models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        tr["title"],
        [tr["diabetes"], tr["heart"], tr["parkinsons"]],
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

st.markdown(f"""
    <h1 style='text-align:center; color:#4B8BBE;'>{tr['title']}</h1>
    <hr style='border: 2px solid #4B8BBE;'>
""", unsafe_allow_html=True)

# ---------------------- Diabetes Prediction ----------------------
if selected == tr["diabetes"]:
    st.subheader(tr["diabetes"] + ' using ML')

    with st.form("diabetes_form"):
        col1, col2, col3 = st.columns(3)
        with col1: Pregnancies = st.number_input('Pregnancies', min_value=0)
        with col2: Glucose = st.number_input('Glucose', min_value=0.0)
        with col3: BloodPressure = st.number_input('Blood Pressure', min_value=0.0)
        with col1: SkinThickness = st.number_input('Skin Thickness', min_value=0.0)
        with col2: Insulin = st.number_input('Insulin', min_value=0.0)
        with col3: BMI = st.number_input('BMI', min_value=0.0)
        with col1: DPF = st.number_input('Diabetes Pedigree Function', min_value=0.0)
        with col2: Age = st.number_input('Age', min_value=1)

        submit = st.form_submit_button(tr["diab_result_btn"])

    if submit:
        input_data = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DPF, Age]
        prediction = diabetes_model.predict([input_data])[0]
        if prediction == 0:
            st.success(tr["diab_no"])
        else:
            st.error(tr["diab_yes"])
            st.info(tr["diab_tips"])

# ---------------------- Heart Disease Prediction ----------------------
elif selected == tr["heart"]:
    st.subheader(tr["heart"] + ' using ML')

    with st.form("heart_form"):
        col1, col2, col3 = st.columns(3)
        with col1: age = st.number_input('Age', min_value=1)
        with col2: sex = st.selectbox('Sex(0-Female ,1-Male)', [0, 1])
        with col3: cp = st.selectbox('Chest Pain Type', [0, 1, 2, 3])
        with col1: trestbps = st.number_input('Resting BP', min_value=0.0)
        with col2: chol = st.number_input('Cholesterol', min_value=0.0)
        with col3: fbs = st.selectbox('Fasting Sugar > 120', [0, 1])
        with col1: restecg = st.selectbox('ECG Result', [0, 1, 2])
        with col2: thalach = st.number_input('Max Heart Rate', min_value=0.0)
        with col3: exang = st.selectbox('Exercise Angina', [0, 1])
        with col1: oldpeak = st.number_input('Oldpeak', min_value=0.0)
        with col2: slope = st.selectbox('Slope', [0, 1, 2])
        with col3: ca = st.selectbox('CA', [0, 1, 2, 3])
        with col1: thal = st.selectbox('Thal', [0, 1, 2])

        submit = st.form_submit_button(tr["heart_result_btn"])

    if submit:
        input_data = [age, sex, cp, trestbps, chol, fbs, restecg,
                      thalach, exang, oldpeak, slope, ca, thal]
        prediction = heart_disease_model.predict([input_data])[0]
        if prediction == 0:
            st.success(tr["heart_no"])
        else:
            st.error(tr["heart_yes"])
            st.info(tr["heart_tips"])

# ---------------------- Parkinson's Prediction ----------------------
elif selected == tr["parkinsons"]:
    st.subheader(tr["parkinsons"] + ' using ML')

    with st.form("parkinsons_form"):
        inputs = []
        for i, label in enumerate([
            'MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)',
            'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer', 'MDVP:Shimmer(dB)',
            'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR',
            'RPDE', 'DFA', 'spread1', 'spread2', 'D2', 'PPE'
        ]):
            if i % 3 == 0:
                col1, col2, col3 = st.columns(3)
            col = [col1, col2, col3][i % 3]
            with col:
                inputs.append(st.number_input(label))

        submit = st.form_submit_button(tr["parkinsons_result_btn"])

    if submit:
        prediction = parkinsons_model.predict([inputs])[0]
        if prediction == 0:
            st.success(tr["park_no"])
        else:
            st.error(tr["park_yes"])
            st.info(tr["parkinsons_tips"])
