# ❤️ Heart Disease Prediction

## 📌 Project Description

Heart Disease Prediction is a Machine Learning project that predicts whether a patient has a high or low risk of heart disease based on medical parameters. The project uses the Random Forest Classifier for accurate prediction and provides a user-friendly Streamlit web application for easy interaction.

---

## 🎯 Objective

To develop a machine learning model that assists in predicting the likelihood of heart disease using patient health information.

---

## 🩺 Features

- Predicts Heart Disease Risk
- Clean and Interactive Streamlit Interface
- Real-Time Prediction
- Displays Prediction Confidence
- Health Recommendations
- Patient Input Summary
- Responsive User Interface

---

## 📊 Dataset

**Dataset Name:** Heart Disease Dataset

### Input Features

- Age
- Sex
- Chest Pain Type (cp)
- Resting Blood Pressure (trestbps)
- Cholesterol (chol)
- Fasting Blood Sugar (fbs)
- Resting ECG (restecg)
- Maximum Heart Rate (thalach)
- Exercise Induced Angina (exang)
- Old Peak
- Slope
- Number of Major Vessels (ca)
- Thal

### Target

- 0 → Low Risk of Heart Disease
- 1 → High Risk of Heart Disease

---

## 🤖 Machine Learning Algorithm

**Random Forest Classifier**

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib
- Matplotlib

---

## 📂 Project Structure

```
Heart-Disease-Prediction
│
├── app.py
├── Heart_Disease.ipynb
├── heart.csv
├── heart_disease_model.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Heart-Disease-Prediction.git
```

Go to the project folder

```bash
cd Heart-Disease-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📈 Model Performance

| Model | Accuracy |
|--------|----------|
| Random Forest | **85.25%** |
| Logistic Regression | 81.97% |
| Decision Tree | 70.49% |

---

## 💡 Prediction Output

The application predicts:

- ✅ Low Risk of Heart Disease
- ⚠️ High Risk of Heart Disease

It also displays:

- Prediction Confidence
- Patient Details
- Health Recommendations

---

## 👨‍💻 Developed By

**Rahul krishna**

B.Tech Information Technology

Machine Learning Mini Project
