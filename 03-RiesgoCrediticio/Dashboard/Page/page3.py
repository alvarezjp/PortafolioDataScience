import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

def pag3(df,test_data,roc_data):
    st.header("Análisis Global del Modelo (Test Set)")

    global_threshold = st.slider(
        "Selecciona threshold para análisis global",
        0.0, 1.0, 0.5, 0.01,
        key="global" 
    )

    
    test_data["y_pred"] = (test_data["y_proba"] >= global_threshold).astype(int)

    test_data

    from sklearn.metrics import confusion_matrix, precision_score, recall_score, accuracy_score

    cm = confusion_matrix(test_data["y_true"], test_data["y_pred"])
    precision = precision_score(test_data["y_true"], test_data["y_pred"])
    recall = recall_score(test_data["y_true"], test_data["y_pred"])
    accuracy = accuracy_score(test_data["y_true"], test_data["y_pred"])
    approval_rate = (test_data["y_pred"] == 0).mean()

    col1, col2, col3 ,col4 = st.columns(4)

    col1.metric("Precision", f"{precision:.3f}")
    col2.metric("Recall", f"{recall:.3f}")
    col3.metric("Accuracy", f"{accuracy:.3f}")
    col4.metric("Porcentaje de clientes aprobados", f"{approval_rate:.1%}")

    labels = ["Cumplido", "En mora"]
    col1,col2 = st.columns([2,1.5])
    with col1:
        fig_cm = px.imshow(
            cm,
            text_auto=True,
            color_continuous_scale="Blues",
            x=labels,
            y=labels,
            title="Matriz de Confusión"
        )

        fig_cm.update_layout(
            xaxis_title="Predicción",
            yaxis_title="Real",
            xaxis=dict(side="top")
        )
        st.plotly_chart(fig_cm,width="stretch")

    with col2:
        fig_roc = go.Figure()

        fig_roc.add_trace(go.Scatter(
            x=roc_data["fpr"],
            y=roc_data["tpr"],
            mode="lines",
            name="ROC Curve"
        ))

        fig_roc.add_trace(go.Scatter(
            x=[0,1],
            y=[0,1],
            mode="lines",
            name="Random",
            line=dict(dash="dash")
        ))

        fig_roc.update_layout(
            title="Curva ROC",
            xaxis_title="False Positive Rate",
            yaxis_title="True Positive Rate"
        )

        st.plotly_chart(fig_roc,width="stretch")



