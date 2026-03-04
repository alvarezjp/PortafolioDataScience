import streamlit as st
import plotly.express as px

def chartBar (df,column,title,xLabel): 
    '''
    Grafico de barra que muestra la cantidad de los elementos que se encuentran dentro de la columna
    '''     

    fig = px.bar(
        df,
        y=column,
        x="cantidad", 
        title=title,
        color=column,
        labels={column: xLabel},
        orientation='h'
        )
    fig.update_layout(showlegend=False)

    st.plotly_chart(fig)

def StackedBarChartTotal (df,column,title):
    '''Agrupa por estatado del incumplimiento, y calcula el porcentaje que comprende'''
    df["loan_status_label"] = df["loan_status"].map({
        1: "Incumple",
        0: "No Incumple"
    })

    
    df_grouped = (
        df.groupby([column, "loan_status_label"])
        .size()
        .reset_index(name="count")
    )

    df_grouped["percentage"] = (
        df_grouped["count"] /
        df_grouped.groupby(column)["count"].transform("sum")
    ) * 100

    
    order = (
        df_grouped
        .groupby(column)["count"]
        .sum()
        .sort_values(ascending=False)
        .index
    )

   
    
    fig_stacked = px.bar(
        df_grouped,
        y=column,
        x="count",
        color="loan_status_label",
        title=title,
        category_orders={
        "loan_status_label": ["No Incumple", "Incumple"],
        column: order
            },
        orientation='h',
         labels={
        "count": "Cantidad de Clientes",
        column: "Categoría",
        "loan_status_label": "Estado del Crédito"
    },
    )
       

    fig_stacked.update_layout(
        barmode='stack',
        height=300, 
        margin=dict(t=40, b=40)
        )
    fig_stacked.update_traces(
    hovertemplate="<b>Cantidad: </b>%{x:,.0f}<extra></extra>"
)

    st.plotly_chart(fig_stacked,width="stretch")

def StackedBarChartPercent (df,column,title):
    '''Agrupa por estatado del incumplimiento, y calcula el porcentaje que comprende'''
    df["loan_status_label"] = df["loan_status"].map({
        1: "Incumple",
        0: "No Incumple"
    })

    # Agrupar por estado de incumplimiento
    df_grouped = (
        df.groupby([column, "loan_status_label"])
        .size()
        .reset_index(name="count")
    )

    df_grouped["percentage"] = (
        df_grouped["count"] /
        df_grouped.groupby(column)["count"].transform("sum")
    ) * 100

    # Calcular total por categoría
    order = (
    df_grouped[df_grouped["loan_status_label"] == "Incumple"]
    .sort_values("percentage", ascending=False)
    [column]
    .tolist()
)

   
    # Gráfico apilado
    fig_stacked = px.bar(
        df_grouped,
        y=column,
        x="percentage",
        color="loan_status_label",
        title=title,
        category_orders={
        "loan_status_label": ["No Incumple", "Incumple"],
        column: order
            },
        orientation='h',
         labels={
        "percentage": "Tasas de incumplimiento %",
        column: "Categoría",
        "loan_status_label": "Estado del Crédito"
    },
    )

    fig_stacked.update_layout(
        barmode='stack',
        height=300,  # mismo alto para todos
        margin=dict(t=40, b=40))
    
    fig_stacked.update_traces(
    hovertemplate="%{x:.1f}%<extra></extra>"
)

    st.plotly_chart(fig_stacked,width="stretch")
    

    

    

