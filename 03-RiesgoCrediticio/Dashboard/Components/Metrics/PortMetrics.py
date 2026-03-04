import streamlit as st
def portfolioMetrics(df):
    # st.subheader('Estado de la Cartera de Crédito')  
    montGroup = df.groupby('loan_status')['loan_amnt'].sum().reset_index()
    montGroup['loan_status_labels']=montGroup['loan_status'].map({
        0:'Cumplidos',
        1:'En mora'
    }
    )

    col1,col2,col3 = st.columns(3)
    with col1:
        st.metric(
            label="Total de Cartera",
            value=montGroup['loan_amnt'][0]+montGroup['loan_amnt'][1],
            border=True,
            format='compact',
        )
    with col2:
        st.metric(
            label="Capital Recuperado (75%)",
            value=montGroup['loan_amnt'][0],
            border=True,
            format='compact'
        )
    
    with col3:
        st.metric(
            label="Capital en Mora (25%)",
            value=montGroup['loan_amnt'][1],
            border=True,
            format='compact'
        )