import streamlit as st
import joblib
import pandas as pd
import time

# ----------------------------
# Load Model
# ----------------------------

model = joblib.load("heart_disease_model.pkl")

# ----------------------------
# Page Configuration
# ----------------------------

st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide"
)

# ----------------------------
# CSS
# ----------------------------

st.markdown("""
<style>

.main{
    background:#F8FAFC;
}

.block-container{
    padding-top:1rem;
}

.title{
    text-align:center;
    color:#C62828;
    font-size:42px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:gray;
    font-size:18px;
}

.stButton>button{

width:100%;

height:55px;

background:#C62828;

color:white;

font-size:18px;

font-weight:bold;

border-radius:12px;

}

.stButton>button:hover{

background:#B71C1C;

color:white;

}

div[data-testid="metric-container"]{

background:#FFF3F3;

padding:15px;

border-radius:12px;

box-shadow:0px 2px 8px rgba(0,0,0,.15);

}

</style>
""",unsafe_allow_html=True)

# ----------------------------
# Sidebar
# ----------------------------

st.sidebar.title("❤️ Heart Disease")

st.sidebar.markdown("---")

st.sidebar.write("### Algorithm")

st.sidebar.success("Random Forest")

st.sidebar.write("### Prediction")

st.sidebar.info("Heart Disease / No Heart Disease")

st.sidebar.write("### Features")

st.sidebar.info("13 Health Parameters")

st.sidebar.markdown("---")

st.sidebar.write("Enter patient details and click Predict.")

# ----------------------------
# Heading
# ----------------------------

st.markdown("""
<p class='title'>
❤️ Heart Disease Prediction
</p>

<p class='subtitle'>
Predict the likelihood of heart disease using patient health information.
</p>
""",unsafe_allow_html=True)

st.divider()

# ----------------------------
# Inputs
# ----------------------------

left,right=st.columns(2)

with left:

    age=st.number_input("Age",20,100,50)

    sex=st.selectbox("Sex",[0,1],format_func=lambda x:"Female" if x==0 else "Male")

    cp=st.selectbox("Chest Pain Type",[0,1,2,3])

    trestbps=st.number_input("Resting Blood Pressure",80,250,120)

    chol=st.number_input("Cholesterol",100,600,200)

    fbs=st.selectbox("Fasting Blood Sugar >120 mg/dl",[0,1])

    restecg=st.selectbox("Resting ECG",[0,1,2])

with right:

    thalach=st.number_input("Maximum Heart Rate",60,220,150)

    exang=st.selectbox("Exercise Induced Angina",[0,1])

    oldpeak=st.number_input("Old Peak",0.0,10.0,1.0)

    slope=st.selectbox("Slope",[0,1,2])

    ca=st.selectbox("Major Vessels",[0,1,2,3,4])

    thal=st.selectbox("Thal",[0,1,2,3])

st.divider()
# ----------------------------
# Prediction
# ----------------------------

if st.button("❤️ Predict"):

    input_df = pd.DataFrame({

        "age":[age],

        "sex":[sex],

        "cp":[cp],

        "trestbps":[trestbps],

        "chol":[chol],

        "fbs":[fbs],

        "restecg":[restecg],

        "thalach":[thalach],

        "exang":[exang],

        "oldpeak":[oldpeak],

        "slope":[slope],

        "ca":[ca],

        "thal":[thal]

    })

    with st.spinner("Analyzing patient data..."):

        time.sleep(2)

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)

    confidence = probability.max()*100

    st.divider()

    c1,c2 = st.columns(2)

    with c1:

        if prediction==0:

            st.balloons()

            st.metric(
                "Prediction",
                "No Heart Disease ✅"
            )

            st.success(
                "The patient is predicted to have no heart disease."
            )

        else:

            st.metric(
                "Prediction",
                "Heart Disease Detected ❤️"
            )

            st.error(
                "The patient is predicted to have heart disease."
            )

    with c2:

        st.metric(
            "Confidence",
            f"{confidence:.2f}%"
        )

        st.progress(int(confidence))

    st.subheader("Patient Details")

    st.dataframe(
        input_df,
        use_container_width=True
    )

    st.subheader("Health Recommendations")

    if prediction==0:

        st.success("""
✔ Maintain a healthy diet

✔ Exercise regularly

✔ Sleep adequately

✔ Continue regular health checkups
""")

    else:

        st.warning("""
• Consult a cardiologist

• Maintain a balanced diet

• Exercise only as advised by your doctor

• Monitor blood pressure and cholesterol

• Take prescribed medications regularly
""")

st.divider()

st.caption("Heart Disease Prediction")