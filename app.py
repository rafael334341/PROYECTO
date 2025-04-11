import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

apgn = pd.read_csv('datos_anteproyecto.csv')
ran = pd.read_csv('datos_random.csv')

st.title('Aplicación 2')

tab1,tab2 =st.tabs(['Tab 1', 'Tab 2'])


with tab1:
    #analisis univariado
    fig, ax = plt.subplots(1,3, figsize=(10,4))
    #educ
    tab_freq = ran['educ'].value_counts().sort_index()
    ax[0].bar((tab_freq.index, tab_freq.values), color='#1f77b4')

    #edad
    ax[1].hist(ran['edad'], bins=40, color='#2ca02c')

    #salario
    ax[2].hist(ran['wage'], bins=40, color='#ff7f0e')

    st.pyplot(fig)

    #analisis bivariado
    fig, ax = plt.subplots(1,2, figsize=(10,4))
    #educ vs wage
    ax[0].scatter(ran['educ'], ran['wage'], color='#d62728')
    #edad vs wage
    ax[1].scatter(ran['edad'], ran['wage'], color='#9467bd')
    st.pyplot(fig)
    
with tab2:
    fig = px.treemap(data_frame = apgn, path=[px.Constant('PGN'), 'Nombre Sector', 'Tipo de gasto'], values='Valor')

    st.plotly_chart(fig)
