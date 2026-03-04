import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
from Page.page1 import pag1
from Page.page2 import pag2
from Page.page3 import pag3
from Page.page4 import pag4

st.set_page_config(
    page_title="Riesgo Crediticio",
    layout="wide" 
)

@st.cache_resource 
def load_model():
    return joblib.load("./Data/modelo_credito.pkl")
model = load_model()

@st.cache_data
def load_df():
    return pd.read_csv('./Data/newDf.csv')
df = load_df()

@st.cache_data
def load_test_results():
    return pd.read_csv("./Data/test_results.csv")
test_data = load_test_results()

@st.cache_data
def load_roc():
    return pd.read_csv("./Data/roc_data.csv")
roc_data = load_roc()

tab1, tab2, tab3, tab4 = st.tabs(["Cartera", "Variables", "Analisis del Modelo","Simulacion Individual"])

with tab1:
    pag1(df)
with tab2:
    pag2(df)
with tab3:
    pag3(df,test_data,roc_data)
with tab4:
    pag4(model)
    







