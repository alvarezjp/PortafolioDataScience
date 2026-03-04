import streamlit as st
from Components.Chart.Chart import chartBar
from Components.Metrics.PortMetrics import portfolioMetrics
def pag1(df):
        st.title('Estado de la cartera de credito')

        col1,col2 = st.columns([1,3])
        
        portfolioMetrics(df)


        conteo = df['loan_status'].value_counts().reset_index()
        conteo.columns = ['loan_status', "cantidad"]
        conteo['loan_status_labels']=conteo['loan_status'].map({
            0:'Cumplidos',
            1:'En mora'
        }
        )
    
        chartBar(conteo,'loan_status_labels','Cantidad de prestamos por estado','Prestamos')