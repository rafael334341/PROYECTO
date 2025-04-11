import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Cargar los datos
apgn = pd.read_csv('datos_anteproyecto.csv')
ran = pd.read_csv('datos_random.csv')

# Título de la aplicación
st.title('Aplicación 2')

# Crear tabs
tab1, tab2 = st.tabs(['Tab 1: Análisis de Datos', 'Tab 2: Treemap PGN'])

# Tab 1 - Análisis de Datos
with tab1:
    st.subheader('Análisis Univariado')
    
    fig, ax = plt.subplots(1, 3, figsize=(15, 4))

    # Distribución educación
    tab_freq = ran['educ'].value_counts().sort_index()
    ax[0].bar(tab_freq.index, tab_freq.values, color='#1f77b4')  # Azul
    ax[0].set_title('Distribución de Educación')
    ax[0].set_xlabel('Años de educación')
    ax[0].set_ylabel('Frecuencia')

    # Distribución edad
    ax[1].hist(ran['edad'], bins=40, color='#2ca02c')  # Verde
    ax[1].set_title('Distribución de Edad')
    ax[1].set_xlabel('Edad')

    # Distribución salario
    ax[2].hist(ran['wage'], bins=40, color='#ff7f0e')  # Naranja
    ax[2].set_title('Distribución de Salario')
    ax[2].set_xlabel('Salario')

    st.pyplot(fig)

    st.subheader('Análisis Bivariado')

    fig, ax = plt.subplots(1, 2, figsize=(15, 4))

    # Educación vs Salario
    ax[0].scatter(ran['educ'], ran['wage'], alpha=0.6, color='#d62728')  # Rojo
    ax[0].set_title('Educación vs Salario')
    ax[0].set_xlabel('Educación')
    ax[0].set_ylabel('Salario')

    # Edad vs Salario
    ax[1].scatter(ran['edad'], ran['wage'], alpha=0.6, color='#9467bd')  # Púrpura
    ax[1].set_title('Edad vs Salario')
    ax[1].set_xlabel('Edad')
    ax[1].set_ylabel('Salario')

    st.pyplot(fig)

# Tab 2 - Treemap PGN
with tab2:
    st.subheader('Distribución del Presupuesto Nacional')
    
    fig = px.treemap(
        data_frame=apgn,
        path=[px.Constant('PGN'), 'Nombre Sector', 'Tipo de gasto'],
        values='Valor',
        color='Valor',
        color_continuous_scale='Agsunset',  # Cambia la escala de colores
        title='Treemap del Anteproyecto PGN'
    )
    
    st.plotly_chart(fig)
