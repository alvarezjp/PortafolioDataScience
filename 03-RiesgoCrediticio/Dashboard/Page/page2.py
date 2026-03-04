import streamlit as st
from Components.Chart.Chart import StackedBarChartTotal,StackedBarChartPercent

def pag2 (df):
    df['person_home_ownership'] = df['person_home_ownership'].replace({
        "RENT": "Arriendo",
        "MORTGAGE": "Hipotecado",
        "OWN": "Propietario",
        "OTHER":"Otros"
    })

    df['rate_pct_bin'] = df['rate_pct_bin'].replace({
            '(5.419, 7.51]':'5.4 - 7.5 %',
            '(7.51, 10.25]':'7.5 - 10.2 %', 
            '(10.25, 11.86]':'10.2 - 11.8 %',
            '(11.86, 13.92]':'11.8 - 13.9 %',
            '(13.92, 23.22]':'13.9 - 23.2 %',
            'Missing':'Valores perdidos'
        })

    df['percentIncome_pct_bin'] = df['percentIncome_pct_bin'].replace({
            '(-0.001, 0.08]':'< 8 %',
            '(0.08, 0.12]':'8 - 12 %', 
            '(0.12, 0.18]':'12 - 18 %',
            '(0.18, 0.25]':'18 - 25 %',
            '(0.25, 0.83]':'25 - 83 %',
        })

    df['cb_person_default_on_file'] = df['cb_person_default_on_file'].replace({
        "N": "No",
        "Y": "Si",
    })

    mostrar_graficos = st.toggle("Normalizar Graficos")

    if not mostrar_graficos :
        st.title("Graficos por cantidad de clientes")
        col1,col2 = st.columns(2)
        with col1:
            StackedBarChartTotal(df,'cb_person_default_on_file','Incumplimiento en Historial')
            StackedBarChartTotal(df,'person_home_ownership','Tipo de vivienda')
        with col2:
            StackedBarChartTotal(df,'rate_pct_bin','Por tasa de interes')
            StackedBarChartTotal(df,'percentIncome_pct_bin','Por tasa de Ingreso')
    if mostrar_graficos:
        st.title("Graficos normalizados")
        col1,col2 = st.columns(2)
        with col1:
            StackedBarChartPercent(df,'cb_person_default_on_file','Incumplimiento en Historial')
            StackedBarChartPercent(df,'person_home_ownership','Tipo de vivienda')
        with col2:
            StackedBarChartPercent(df,'rate_pct_bin','Por tasa de interes')
            StackedBarChartPercent(df,'percentIncome_pct_bin','Por tasa de Ingreso')