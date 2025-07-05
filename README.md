# 🧠 Multi-Disease Prediction App

This is a **Streamlit-based web application** that uses **machine learning models** to predict the likelihood of three common diseases:

- ❤️ Heart Disease
- 🩸 Diabetes
- 🧠 Parkinson’s Disease

Built using `scikit-learn`, `Streamlit`, and `Python`, this app allows users to enter medical data and instantly see predictions in **English, Hindi, or Telugu**.

## 🚀 Live Demo

Access the deployed app here:  
👉 [multi-disease-ml-app-by-prasannakumarreddy.streamlit.app](https://multi-disease-prediction-ml-app-by-prasannakumarreddy.streamlit.app/)

## 📋 Features

- 🧮 Predict diseases using pre-trained `.pkl` models
- 🔘 Sidebar navigation using `streamlit-option-menu`
- ✅ Real-time results from user input
- 💡 Simple and intuitive UI for non-technical users

## 🛠️ Tech Stack

- **Frontend**: Streamlit, streamlit-option-menu
- **Backend**: Python, scikit-learn
- **ML Models**: Logistic Regression / SVM / Random Forest (pre-trained and saved as `.pkl`)
- **Deployment**: Streamlit Cloud

## 📦 Installation (Local Setup)

```bash
git clone https://github.com/PrasannaKumar260904/multi-disease-ml-app.git
cd multi-disease-ml-app
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
streamlit run mdps_public.py
```

> ✅ Make sure the `.pkl` model files are placed correctly in the `models/` folder or root directory.

## 🧪 Sample Input Fields

Each disease module accepts common diagnostic features:

- **Heart Disease**: Age, Sex, Chest Pain Type, Cholesterol, Fasting Blood Sugar, etc.
- **Diabetes**: Pregnancies, Glucose Level, BMI, Diabetes Pedigree Function, etc.
- **Parkinson’s**: MDVP:Fo(Hz), Jitter(%), Shimmer(dB), NHR, HNR, etc.

## 📁 Project Structure

```
multi-disease-ml-app/
│
├── mdps_public.py               # Main Streamlit app
├── requirements.txt             # Python dependencies
├── .streamlit/
│   └── config.toml              # Streamlit cloud configuration
├── models/
│   ├── heart_disease_model.sav
│   ├── diabetes_model.sav
│   └── parkinsons_model.sav
└── README.md
```

## 🙋‍♂️ Author

**Prasanna Kumar Reddy Dodla**  
📧 prasannakumarreddy003@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/prasannakumarreddy003)  
🔗 [GitHub](https://github.com/PrasannaKumar260904)

## ⭐️ Show Your Support

If you found this project helpful:

- ⭐ Star this repository
- 🍴 Fork it to use or contribute
- 📢 Share it with others in the ML or healthcare space
