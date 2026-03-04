import streamlit as st
import pandas as pd
def pag4(model):
    calculo=0.0
    st.header(f"🧍 Simulación Individual")

    col1, col2 = st.columns(2)

    with col1:
        person_age = st.number_input("Edad", 18, 100, 30)
        person_income = st.number_input("Ingreso anual", 0, 90000000)
        loan_amnt = st.number_input("Monto préstamo", 0, 1000000)
        loan_int_rate = st.number_input("Tasa interés", 0.0, 10.0)

    with col2:
        person_emp_length = st.number_input("Años trabajando", 0.0, 85.0)
        if(person_income != 0):
            calculo = (loan_amnt/person_income )
       

     
        home_ownership_options = {
        "Arrienda": "RENT",
        "Propietario": "OWN",
        "Hipotecada": "MORTGAGE",
        "Otro": "OTHER"
    }

        selected_home_label = st.selectbox(
            "Tipo de vivienda",
            options=list(home_ownership_options.keys())
        )

        person_home_ownership = home_ownership_options[selected_home_label]

        loan_intent_options = {
        "Uso personal": "PERSONAL",
        "Educación": "EDUCATION",
        "Gastos médicos": "MEDICAL",
        "Emprendimiento": "VENTURE",
        "Mejora del hogar": "HOMEIMPROVEMENT",
        "Consolidación de deudas": "DEBTCONSOLIDATION"
    }

        selected_label = st.selectbox(
            "Propósito del préstamo",
            options=list(loan_intent_options.keys())
        )

        loan_intent = loan_intent_options[selected_label]

        cb_person_default_on_file_options = {
        "No": "N",
        "Si": "Y",
        }

        selected_label_perDefault = st.selectbox(
            "Con historial previo de incumplimiento ?",
            options=list(cb_person_default_on_file_options.keys())
        )

        cb_person_default_on_file = cb_person_default_on_file_options[selected_label_perDefault]
    
    st.metric(
        label="Porcentaje del ingreso comprometido",
        value=calculo,
        format="percent",
        width='content',
        border=True
           )
    threshold = st.slider("Umbral decisión", 0.0, 1.0, 0.5, 0.01)

    # ===== Prediccion =====

    if st.button("Predecir riesgo"):

        data = pd.DataFrame({
            "person_age": [person_age],
            "person_income": [person_income],
            "person_emp_length": [person_emp_length],
            "loan_amnt": [loan_amnt],
            "loan_int_rate": [loan_int_rate],
            "loan_percent_income": calculo,
            "cb_person_cred_hist_length": 5,
            "person_home_ownership": [person_home_ownership],
            "loan_intent": [loan_intent],
            "loan_grade": 'A',
            "cb_person_default_on_file": [cb_person_default_on_file]
        })

        proba = model.predict_proba(data)[0][1]

        st.subheader("Resultado")

        st.progress(float(proba))

        st.write(f"Probabilidad estimada de default: {proba:.2%}")

        if proba >= threshold:
            st.error("⚠️ Clasificado como Alto Riesgo")
        else:
            st.success("✅ Clasificado como Bajo Riesgo")